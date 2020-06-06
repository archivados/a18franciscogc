# 1: imports of python lib
# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class AccountInvoice(models.Model):
    """Modification of the account.invoice to adapt it to the needs of the module.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _inherit = 'account.invoice'

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Relational Fields
    # -------------------------------------------------------------------------
    incidence_ids = fields.Many2many(
        'xestionsat.incidence',
        string='Invoice',
        ondelete='restrict',
    )

    ###########################################################################
    # CRUD methods
    ###########################################################################
    @api.multi
    def unlink(self):
        return super(AccountInvoice, self).unlink()

        for incidence in self.incidence_ids:
            incidence.invoice_id = False
