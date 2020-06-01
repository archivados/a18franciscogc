# 1: imports of python lib
# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class AccountInvoice(models.Model):
    """Modification of the account.invoice to adapt it to the needs of the module.
    """

    # Private attributes
    _inherit = 'account.invoice'

    # Default methods

    # Fields declaration
    # Relational Fields
    incidence_id = fields.Many2one(
        'xestionsat.incidence',
        string='Invoice',
    )

    # Other Fields

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges

    # CRUD methods

    # Action methods

    # Business methods
