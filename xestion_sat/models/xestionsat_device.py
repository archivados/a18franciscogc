# 1: imports of python lib
from datetime import datetime

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class Device(models.Model):
    """Model to manage the information of a device.
    """

    # Private attributes
    _name = 'xestionsat.device'
    _description = _('Device associated with a Customer')
    _rec_name = 'name'
    _order = 'owner_id, internal_id, name'

    # Default methods

    # Fields declaration
    # Relational Fields
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
    incidence_ids = fields.Many2many(
        'xestionsat.incidence',
        string='Related Incidences',
    )

    # Other Fields
    name = fields.Char(
        string='Name',
        required=True,
    )
    internal_id = fields.Char(
        string='Internal ID',
    )
    location = fields.Char(
        string='Location',
    )
    description = fields.Char(
        string='Description',
    )
    observation = fields.Char(
        string='Observations',
    )

    date_registration = fields.Date(
        string='Date of registration',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d'),
        required=True,
    )
    date_cancellation = fields.Date(
        string='Date of cancellation'
    )

    state = fields.Selection(
        [
            ('stored', 'Stored'),
            ('operational', 'Operational'),
            ('repairing', 'Repairing'),
            ('unsubscribe', 'Unsubscribe'),
        ],
        string='State',
        default="operational",
        required=True,
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges
    @api.constrains('headquarter_id')
    def _check_headquarter(self):
        """Check that the Headquarters entered correspond with the current customer.
        """

        for device in self:
            if device.headquarter_id \
                and device.headquarter_id.parent_id != device.owner_id \
                    and device.headquarter_id != device.owner_id:
                raise models.ValidationError(
                    _('The Headquarters must belong to the specified Customer')
                )

    @api.constrains('user_ids')
    def _check_users(self):
        """Verify that the users entered correspond to the current customer.
        """

        error_message = 'The Device User must be a member  of the specified' \
            ' Customer'

        for device in self:
            for user in device.user_ids:
                if user.parent_id != device.owner_id \
                        and user != device.owner_id:
                    raise models.ValidationError(_(error_message))

    @api.constrains('internal_id')
    def _check_internal_id(self):
        """Check that the internal_id is not repeated.
        """

        for device in self:
            if device.internal_id and self.env['xestionsat.device'].search(
                [('internal_id', '=', self.internal_id), ('id', '!=', self.id)]
            ):
                raise ValueError(_('The code already exists'))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        """Verify that device creation is not assigned to a different system
        user than the one running the application.
        """

        error_message = 'One User cannot create Devices in the name of another'

        for device in self:
            if device.created_by_id and device.created_by_id != self.env.user:
                raise models.ValidationError(_(error_message))

    # CRUD methods

    # Action methods
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
                    mensaxe = _('Moving from %s to %s is not allowed') \
                        % (device.state, new_state)
                    raise models.UserError(mensaxe)

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

        return self.create_new_incidence()

    def make_unsubscribe(self):
        """Invokes the change of state to unsubscribe.
        """

        self.change_state('unsubscribe')

    @api.multi
    def create_new_incidence(self):
        """Method to create a new incidence with the data of the current device.
        """

        incidence_form = self.env.ref('xestionsat.incidence', False)

        new_incidence_context = {
            'default_lock': True,
            'default_customer_id': self.owner_id.id,
            'default_device_ids': [self.id],
        }

        new_incidence_views = [
            (incidence_form, 'form'),
        ]

        new_incidence_flags = {
            'action_buttons': True,
        }

        new_incidence = {
            'name': _('New incidence'),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.incidence',
            'view_type': 'form',
            'view_mode': 'form',
            'context': new_incidence_context,
            'target': 'new',
            'views': new_incidence_views,
            'view_id': incidence_form,
            'flags': new_incidence_flags,
        }

        return new_incidence

    @api.multi
    def add_component(self):
        """Method to add a new component for the current device.
        """

        component_form = self.env.ref('xestionsat.device.component', False)

        add_component_context = {
            'default_device_id': self.id,
        }

        add_component_views = [
            (component_form, 'form'),
        ]

        add_component_flags = {
            'action_buttons': True,
        }

        add_component = {
            'name': _('Add component'),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.device.component',
            'view_type': 'form',
            'view_mode': 'form',
            'context': add_component_context,
            'target': 'new',
            'views': add_component_views,
            'view_id': component_form,
            'flags': add_component_flags,
        }

        return add_component

    # Business methods
