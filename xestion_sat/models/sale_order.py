# 1: imports of python lib
# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class SaleOrder(models.Model):
    """Modification of the res.partner to adapt it to the needs of the module.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _inherit = 'sale.order'

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Relational Fields
    # -------------------------------------------------------------------------
    incidence_ids = fields.Many2many(
        'xestionsat.incidence',
        string='Order',
        ondelete='restrict',
    )
