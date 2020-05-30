# 1: imports of python lib
from lxml import etree

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules
from .xestionsat_common import NEW_DEVICE
from .xestionsat_common import STATE_DEVICE

# 5: local imports

# 6: Import of unknown third party lib


class Device(models.Model):
    """Model to manage the information of a device.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _name = 'xestionsat.device'
    _description = _('Device associated with a Customer')
    _rec_name = 'name'
    _order = 'owner_id, internal_id, name'

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
    )
    user_ids = fields.Many2many(
        'res.partner',
        string='Users',
    )
    devicecomponent_ids = fields.One2many(
        'xestionsat.device.component',
        string='Device Components',
        inverse_name='device_id',
    )
    othterdata_ids = fields.One2many(
        'xestionsat.device.other_data',
        string='Other data',
        inverse_name='device_id',
    )
    incidence_ids = fields.Many2many(
        'xestionsat.incidence',
        string='Related Incidences',
        ondelete='restrict',
    )

    # -------------------------------------------------------------------------
    # Other Fields
    # -------------------------------------------------------------------------
    name = fields.Char(
        string='Name',
        required=True,
        index=True,
    )
    internal_id = fields.Char(
        string='Internal ID',
        index=True,
    )
    location = fields.Char(
        string='Location',
    )
    description = fields.Text(
        string='Description',
    )
    observation = fields.Text(
        string='Observations',
    )

    date_registration = fields.Datetime(
        string='Date of registration',
        default=lambda *a: fields.Datetime.now(),
        required=True,
    )
    date_cancellation = fields.Datetime(
        string='Date of cancellation'
    )

    state = fields.Selection(
        selection=_get_state_items,
        string='State',
        default=_get_default_state,
        required=True,
    )

    ###########################################################################
    # compute and search fields, in the same order that fields declaration
    ###########################################################################

    ###########################################################################
    # Constraints and onchanges
    ###########################################################################
    @api.constrains('headquarter_id')
    def _check_headquarter(self):
        """Check that the Headquarters entered correspond with the current customer.
        """
        for record in self:
            if record.headquarter_id \
                and record.headquarter_id.parent_id != record.owner_id \
                    and record.headquarter_id != record.owner_id:
                raise models.ValidationError(
                    _('The Headquarters must belong to the specified Customer')
                )

    @api.constrains('user_ids')
    def _check_users(self):
        """Verify that the users entered correspond to the current customer.
        """
        error_message = 'The Device User must be a member  of the specified' \
            ' Customer'

        for record in self:
            for user in record.user_ids:
                if user.parent_id != record.owner_id \
                        and user != record.owner_id:
                    raise models.ValidationError(_(error_message))

    @api.constrains('internal_id')
    def _check_internal_id(self):
        """Check that the internal_id is not repeated.
        """
        for record in self:
            if record.internal_id and self.env['xestionsat.device'].search(
                [('internal_id', '=', self.internal_id), ('id', '!=', self.id)]
            ):
                raise ValueError(_('The code already exists'))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        """Verify that device creation is not assigned to a different system
        user than the one running the application.
        """
        error_message = 'One User cannot create Devices in the name of another'

        for record in self:
            if record.created_by_id and record.created_by_id != self.env.user:
                raise models.ValidationError(_(error_message))

    @api.constrains('date_registration', 'date_cancellation')
    def _check_date_end(self):
        """Check that the cancellation date is not earlier than the start registration.
        """
        error_message = 'The cancellation date cannot be earlier than the' \
            ' registration date'

        for record in self:
            if record.date_cancellation:
                if record.date_cancellation < record.date_registration:
                    raise models.ValidationError(_(error_message))

    ###########################################################################
    # CRUD methods
    ###########################################################################
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

    ###########################################################################
    # Action methods
    ###########################################################################
    @api.model
    def is_allowed_transition(self, actual_state, new_state):
        """Handles allowed state changes.

        :param actual_state: Currently assigned status.
        :param new_state: New state to be assigned.
        """
        allowed = [
            ('stored', 'operational'),
            ('stored', 'repairing'),
            ('stored', 'unsubscribe'),

            ('operational', 'stored'),
            ('operational', 'repairing'),
            ('operational', 'unsubscribe'),

            ('repairing', 'stored'),
            ('repairing', 'operational'),
            ('repairing', 'unsubscribe'),

            ('unsubscribe', 'stored'),
            ('unsubscribe', 'operational'),
            ('unsubscribe', 'repairing')
        ]
        return (actual_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        """Apply a change of status.
        :param new_state: New state to be assigned.
        """
        for device in self:
            if device.state != new_state:
                if device.is_allowed_transition(device.state, new_state):
                    device.state = new_state
                else:
                    error_message = _('Moving from %s to %s is not allowed') \
                        % (device.state, new_state)
                    raise models.UserError(error_message)

    def make_stored(self):
        """Invokes the change of state to stored.
        """
        self.change_state('stored')

    def make_operational(self):
        """Invokes the change of state to operational.
        """
        self.change_state('operational')

    @api.multi
    def create_incidence(self):
        """Invokes the change of state to repairing and launches the method to
        create a new incidence.
        """
        self.change_state('repairing')

        return self.add_incidence()

    def make_unsubscribe(self):
        """Invokes the change of state to unsubscribe.
        """
        self.change_state('unsubscribe')

    @api.multi
    def add_incidence(self):
        """Method to create a new incidence with the data of the current device.
        """
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
    def fields_view_get(self, view_id=None, view_type=None, **kwargs):
        """Modify the resulting view according to user preferences.
        """
        context = self.env.context

        result = super(Device, self).fields_view_get(
            view_id=view_id, view_type=view_type, **kwargs
        )

        if view_type == 'form':
            lock = False

            if 'lock_view' in context:
                lock = context['lock_view']

            if lock:
                doc = etree.XML(result['arch'])

                # Form
                for node in doc.xpath("//form[@name='primary_form']"):
                    node.set('create', 'false')
                    node.set('edit', 'false')

                # owner_id
                for node in doc.xpath("//field[@name='owner_id']"):
                    node.set('modifiers', '{"readonly": true}')

                # btn_close
                for node in doc.xpath("//button[@name='btn_close']"):
                    # node.set('invisible', 'False')
                    node.set('modifiers', '{}')

                result['arch'] = etree.tostring(doc)
        return result
