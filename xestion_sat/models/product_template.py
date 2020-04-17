# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class ProductTemplate(models.Model):
    # Private attributes
    _inherit = 'product.template'

    # Default methods

    # Fields declaration
    # Relational Fields
    type = fields.Selection(
        [
            ('consu', 'Consumable'),
            ('service', 'Service'),
            ('sat', 'TAS Action'),
        ],
        string='Type',
        default="consu",
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges