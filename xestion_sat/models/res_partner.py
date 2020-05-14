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
    def add_incidence(self):
        """Method to create a new incidence with the data of the current partner.
        """

        context = {
            'lock_view': True,
            'default_customer_id': self.id,
        }

        flags = {
            'action_buttons': True,
        }

        return self.env['xestionsat.incidence'].create_new_incidence(
            context=context, flags=flags)

    @api.multi
    def add_device(self):
        """Method to create a new device with the data of the current partner.
        """

        context = {
            'lock_view': True,
            'default_owner_id': self.id,
        }

        flags = {
        }

        return self.env['xestionsat.device'].create_new_device(
            context=context, flags=flags)

    # Business methods
