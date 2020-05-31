# 1: imports of python lib
# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class SaleOrder(models.Model):
    """Modification of the res.partner to adapt it to the needs of the module.
    """

    # Private attributes
    _inherit = 'sale.order'

    # Default methods

    # Fields declaration
    # Relational Fields
    incidence_id = fields.Many2one(
        'xestionsat.incidence',
        string='Order',
    )

    # Other Fields

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges

    # CRUD methods

    # Action methods

    # Business methods
