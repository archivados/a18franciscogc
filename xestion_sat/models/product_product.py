# 1: imports of python lib
# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class ProductTemplate(models.Model):
    """Modification of the product.template to adapt it to the needs of the module.
    """
    ###########################################################################
    # Private attributes
    _inherit = 'product.product'
    _order = 'type desc, name'
