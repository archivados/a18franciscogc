# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class Device(models.Model):
    # Private attributes
    _name = 'xestionsat.device'
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
    devicecomponents_ids = fields.One2many(
        'xestionsat.device.component',
        string='Device Components',
        inverse_name='device_id',
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
        'Date of registration',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d'),
    )
    date_cancellation = fields.Date('Date of cancellation')

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
    @api.model
    def is_allowed_transition(self, actual_state, new_state):
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
        for device in self:
            if device.state != new_state:
                if device.cambios_estado_permitidos(device.state, new_state):
                    device.state = new_state
                else:
                    mensaxe = _('Moving from %s to %s is not allowed') % (device.state, new_state)
                    raise models.UserError(mensaxe)

    def make_stored(self):
        self.change_state('stored')

    def make_operational(self):
        self.change_state('operational')

    @api.multi
    def create_incidence(self):
        self.change_state('repairing')

        return self.create_new_incidence()

    def make_unsubscribe(self):
        self.change_state('unsubscribe')

    '''
    @api.multi
    def comprobar_incidences(self):
        ten_incidences = False

        for incidence in self.env['xestionsat.incidence'].search([]):
            domain = ['&',('device.id', 'in', incidence.device_ids), ('state', '=', 'repairing')]
            ten_incidences = self.env['xestionsat.incidence'].search(domain, count=True) > 0

        return ten_incidences
    '''

    @api.multi
    def create_new_incidence(self):
        incidence_form = self.env.ref('xestionsat.incidence', False)

        new_incidence_context = {
            'default_bloquear': True,
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

        # record = self.env['xestionsat.incidence'].create(new_incidence)
        return new_incidence

    # Constraints and onchanges
    @api.constrains('headquarter_id')
    def _check_headquarter(self):
        for device in self:
            if device.headquarter_id and device.headquarter_id.parent_id != device.owner_id and device.headquarter_id != device.owner_id:
                raise models.ValidationError(_('The Headquarters must belong to the specified Customer'))

    @api.constrains('user_ids')
    def _check_users(self):
        for device in self:
            for user in device.user_ids:
                if user.parent_id != device.owner_id and user != device.owner_id:
                    raise models.ValidationError(_('The Device User must be a member of the specified Customer'))

    @api.constrains('internal_id')
    def _check_internal_id(self):
        for device in self:
            if device.internal_id and self.env['xestionsat.device'].search([('internal_id', '=', self.internal_id), ('id', '!=', self.id)]):
                raise ValueError(_('The code already exists'))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        for device in self:
            if device.created_by_id and device.created_by_id != self.env.user:
                raise models.ValidationError(_('One User cannot create Devices in the name of another'))


    # CRUD methods

    # Action methods

    # Business methods
