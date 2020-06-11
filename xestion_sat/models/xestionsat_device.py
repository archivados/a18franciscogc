# 1: imports of python lib
from lxml import etree

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules
from .xestionsat_common import compare_list, message_post_list

from .xestionsat_common import NEW_DEVICE
from .xestionsat_common import STATE_DEVICE

from .xestionsat_message import MESSAGE

# 5: local imports

# 6: Import of unknown third party lib


class Device(models.Model):
    """Model to manage the information of a device.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _name = 'xestionsat.device'
    _description = _('Device')
    _rec_name = 'name'
    _order = 'owner_id, internal_id, name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ###########################################################################
    # Default methods
    ###########################################################################
    @api.model
    def _get_state_items(self):
        """ Get the values for state.
        """
        return STATE_DEVICE

    @api.model
    def _get_default_state(self):
        """ Gives default state.
        """
        return STATE_DEVICE[0][0]

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Relational Fields
    # -------------------------------------------------------------------------
    created_by_id = fields.Many2one(
        'res.users',
        string='Created by',
        ondelete='restrict',
        default=lambda self: self.env.user,
        required=True,
        track_visibility='onchange',
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        ondelete='cascade',
        required=True,
    )
    headquarter_id = fields.Many2one(
        'res.partner',
        string='Headquarters address',
        ondelete='restrict',
        required=True,
        track_visibility='onchange',
    )
    user_ids = fields.Many2many(
        'res.partner',
        string='Users',
        track_visibility='onchange',
    )
    devicecomponent_ids = fields.One2many(
        'xestionsat.device.component',
        string='Device Components',
        inverse_name='device_id',
        ondelete='cascade',
        track_visibility='onchange',
    )
    othter_data_ids = fields.One2many(
        'xestionsat.device.other_data',
        string='Other data',
        inverse_name='device_id',
        ondelete='cascade',
        track_visibility='onchange',
    )
    incidence_ids = fields.Many2many(
        'xestionsat.incidence',
        string='Related Incidences',
        ondelete='restrict',
        track_visibility='onchange',
    )

    # -------------------------------------------------------------------------
    # Other Fields
    # -------------------------------------------------------------------------
    name = fields.Char(
        string='Name',
        required=True,
        index=True,
        track_visibility='onchange',
    )
    internal_id = fields.Char(
        string='Internal ID',
        index=True,
        track_visibility='onchange',
    )
    location = fields.Char(
        string='Location',
        track_visibility='onchange',
    )
    description = fields.Text(
        string='Description',
        track_visibility='onchange',
    )
    observation = fields.Text(
        string='Observations',
        track_visibility='onchange',
    )

    date_registration = fields.Datetime(
        string='Registration date',
        default=lambda *a: fields.Datetime.now(),
        required=True,
        track_visibility='onchange',
    )
    date_cancellation = fields.Datetime(
        string='Cancellation Date',
        track_visibility='onchange',
    )

    state = fields.Selection(
        string='State',
        selection=_get_state_items,
        default=_get_default_state,
        required=True,
        track_visibility='onchange',
    )

    ###########################################################################
    # compute and search fields, in the same order that fields declaration
    ###########################################################################

    ###########################################################################
    # Constraints and onchanges
    ###########################################################################

    # -------------------------------------------------------------------------
    # constrains
    # -------------------------------------------------------------------------
    @api.constrains('headquarter_id')
    def _check_headquarter(self):
        """Check that the Headquarters entered correspond with the current customer.
        """
        for record in self:
            if record.headquarter_id \
                and record.headquarter_id.parent_id != record.owner_id \
                    and record.headquarter_id != record.owner_id:
                raise models.ValidationError(
                    _(MESSAGE['device_constraint']['headquarter_id']))

    @api.constrains('user_ids')
    def _check_users(self):
        """Verify that the users entered correspond to the current customer.
        """
        for record in self:
            for user in record.user_ids:
                if user.parent_id != record.owner_id \
                        and user != record.owner_id:
                    raise models.ValidationError(
                        _(MESSAGE['device_constraint']['user_ids']))

    @api.constrains('internal_id')
    def _check_internal_id(self):
        """Check that the internal_id is not repeated.
        """
        for record in self:
            if record.internal_id and self.env['xestionsat.device'].search(
                [('internal_id', '=', self.internal_id), ('id', '!=', self.id)]
            ):
                raise models.ValidationError(
                    _(MESSAGE['device_constraint']['internal_id']))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        """Verify that device creation is not assigned to a different system
        user than the one running the application.
        """
        for record in self:
            if record.created_by_id and record.created_by_id != self.env.user:
                raise models.ValidationError(
                    _(MESSAGE['device_constraint']['created_by_id']))

    @api.constrains('date_registration', 'date_cancellation')
    def _check_date_end(self):
        """Check that the cancellation date is not earlier than the start registration.
        """
        for record in self:
            if record.date_cancellation:
                if record.date_cancellation < record.date_registration:
                    raise models.ValidationError(
                        _(MESSAGE['device_constraint']['date_cancellation']))

    # -------------------------------------------------------------------------
    # Onchange
    # -------------------------------------------------------------------------
    @api.onchange('owner_id')
    def _check_owner_id(self):
        """Check the current owner_id.
        """
        child_ids = self.owner_id.child_ids

        if not self.headquarter_id:
            self.headquarter_id = self.owner_id
        elif self.headquarter_id != self.owner_id \
                and self.headquarter_id not in child_ids:
            self.headquarter_id = self.owner_id

    @api.onchange('state')
    def _check_state(self):
        """Check the current state.
        """
        if len(self.get_active_incidence()) > 0:
            raise models.ValidationError(
                _(MESSAGE['device_constraint']['in_active_incidence']))

        # Repair state
        if self.state == STATE_DEVICE[1][0]:
            raise models.ValidationError(
                _(MESSAGE['device_constraint']['repairing']))

        # Unsubscribe state
        if self.state == STATE_DEVICE[3][0]:
            self.date_cancellation = fields.Datetime.now()
        else:
            self.date_cancellation = False

    ###########################################################################
    # CRUD methods
    ###########################################################################
    @api.multi
    def write(self, vals):
        # Components Tracking
        old_components = self.devicecomponent_ids
        components_msg = ''

        if 'devicecomponent_ids' in vals:
            if len(old_components) > 0:
                components_msg += '<b>Old Components</b><ul>'
                for componnet in old_components:
                    components_msg += message_post_list(
                        {
                            'Componnet:': componnet.product_id.display_name,
                            'serial:': componnet.serial,
                            'Registration Date:': componnet.date_registration,
                            'Cancellation Date:': componnet.date_cancellation,
                        }
                    )

        # Other Data Tracking
        old_data = self.othter_data_ids
        data_msg = ''

        if 'othter_data_ids' in vals:
            if len(old_data) > 0:
                data_msg += '<b>Old Data</b><ul>'
                for data in old_data:
                    data_msg += message_post_list(
                        {
                            'Data:': data.data,
                            'Value:': data.value,
                            'Registration Date:': data.date_registration,
                        }
                    )

        super(Device, self).write(vals)

        # Components Tracking
        if not compare_list(old_components, self.devicecomponent_ids):
            components_msg += '</ul><b>New Components</b><ul>'

            for componnet in self.devicecomponent_ids:
                components_msg += message_post_list(
                    {
                        'Componnet:': componnet.product_id.display_name,
                        'serial:': componnet.serial,
                        'Registration Date:': componnet.date_registration,
                        'Cancellation Date:': componnet.date_cancellation,
                    }
                )

            self.message_post(body=_(components_msg) + '</ul>')

        # Other Data Tracking
        if not compare_list(old_data, self.othter_data_ids):
            data_msg += '</ul><b>New Data</b><ul>'

            for data in self.othter_data_ids:
                data_msg += message_post_list(
                    {
                        'Data:': data.data,
                        'Value:': data.value,
                        'Registration Date:': data.date_registration,
                    }
                )

            self.message_post(body=_(data_msg) + '</ul>')

    @api.multi
    def create_new_device(
        self, name=NEW_DEVICE, context=None, flags=None
    ):
        """Method to create a new device according to the past context.

        :param name: View title.
        :param context: Context to present the view data.
        :param flags: Flags to modify the view.
        """
        if type(name) != str:
            name = NEW_DEVICE

        return {
            'name': _(name),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.device',
            'view_type': 'form',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'flags': flags,
        }

    @api.multi
    def unlink(self):
        incidence_obj = self.env['xestionsat.incidence']
        incidence_devices = incidence_obj.search(
            [('device_ids', 'in', self.ids)])
        if incidence_devices:
            raise models.ValidationError(
                _(MESSAGE['device_constraint']['unlink']))
        return super(Device, self).unlink()

    ###########################################################################
    # Action methods
    ###########################################################################
    @api.multi
    def create_incidence(self):
        """Invokes the change of state to repairing and launches the method to
        create a new incidence.
        """
        return self.add_incidence()

    @api.multi
    def add_incidence(self):
        """Method to create a new incidence with the data of the current device.
        """
        if len(self.get_active_incidence()) > 0:
            raise models.ValidationError(
                _(MESSAGE['device_constraint']['in_active_incidence']))

        context = {
            'lock_view': True,
            'default_customer_id': self.owner_id.id,
            'default_device_ids': [self.id],
        }

        flags = {
            'action_buttons': True,
        }

        return self.env['xestionsat.incidence'].create_new_incidence(
            context=context, flags=flags)

    @api.multi
    def add_component(self):
        """Method to add a new component for the current device.
        """
        context = {
            'device_view': True,
            'default_device_id': self.id,
        }

        flags = {
            'action_buttons': True,
        }

        return self.env['xestionsat.device.component'].create_new_component(
            context=context, flags=flags)

    @api.multi
    def add_other_data(self):
        """Method to add a new other data for the current device.
        """
        context = {
            'device_view': True,
            'default_device_id': self.id,
        }

        flags = {
            'action_buttons': True,
        }

        return self.env['xestionsat.device.other_data'].add_new_data(
            context=context, flags=flags)

    ###########################################################################
    # Business methods
    ###########################################################################
    @api.model
    def get_active_incidence(self):
        """Get the active incidences in which the device is.
        """
        stages_locked = self.env['xestionsat.incidence.stage'].search(
            [('lock_incidence', '=', True)])
        stages_locked_ids = []
        for stage in stages_locked:
            stages_locked_ids.append(stage.id)

        active_incidences = []

        incidences = self.env['xestionsat.incidence'].search(
            [('stage_id', 'not in', stages_locked_ids)])
        for incidence in incidences:
            for device_id in incidence.device_ids:
                if self.id == device_id.id:
                    active_incidences.append(incidence.id)
                    break
        return active_incidences

    @api.model
    def fields_view_get(self, view_id=None, view_type=None, **kwargs):
        """Modify the resulting view according to user preferences.
        """
        context = self.env.context

        result = super(Device, self).fields_view_get(
            view_id=view_id, view_type=view_type, **kwargs
        )

        if view_type == 'form':
            lock = False

            doc = etree.XML(result['arch'])

            # incidence page
            # for node in doc.xpath("//page[@name='incidences']"):
            #    node.set('modifiers', '{"invisible": true}')

            if 'lock_view' in context:
                lock = context['lock_view']

            if lock:

                # Form
                for node in doc.xpath("//form[@name='primary_form']"):
                    node.set('create', 'false')
                    node.set('edit', 'false')

                # owner_id
                for node in doc.xpath("//field[@name='owner_id']"):
                    node.set('modifiers', '{"readonly": true}')

                # create_incidence
                for node in doc.xpath("//button[@name='create_incidence']"):
                    node.set('modifiers', '{"invisible": true}')

            result['arch'] = etree.tostring(doc)
        return result
