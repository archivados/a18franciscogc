# 1: imports of python lib
# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class ResPartner(models.Model):
    """Modification of the res.partner to adapt it to the needs of the module.
    """

    # Private attributes
    _inherit = 'res.partner'

    # Default methods

    # Fields declaration
    # Relational Fields
    device_ids = fields.One2many(
        'xestionsat.device',
        string='Devices',
        inverse_name='owner_id',
    )
    incidence_ids = fields.One2many(
        'xestionsat.incidence',
        string='Incidences',
        inverse_name='customer_id',
    )
    # Other Fields

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges

    # CRUD methods

    # Action methods
    @api.multi
    def create_new_incidence(self):
        """Method to create a new incidence with the data of the current partner.
        """

        incidence_form = self.env.ref('xestionsat.incidence.form_readonly', False)

        new_incidence_context = {
            'default_customer_id': self.id,
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
    def create_new_device(self):
        """Method to create a new device with the data of the current partner.
        """

        device_form = self.env.ref('xestionsat.device', False)

        new_device_context = {
            'default_owner_id': self.id,
        }

        new_device_views = [
            (device_form, 'form'),
        ]

        new_device_flags = {
        }

        new_device = {
            'name': _('New device'),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.device',
            'view_type': 'form',
            'view_mode': 'form',
            'context': new_device_context,
            'target': 'new',
            'views': new_device_views,
            'view_id': device_form,
            'flags': new_device_flags,
        }

        return new_device

    # Business methods
