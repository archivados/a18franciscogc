# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class ProductTemplate(models.Model):
    """Modification of the product.template to adapt it to the needs of the module.
    """

    # Private attributes
    _inherit = 'product.template'

    # Default methods

    # Fields declaration
    # Relational Fields
    # Other Fields
    type = fields.Selection(
        [
            ('consu', 'Consumable'),
            ('service', 'Service'),
            ('sat', 'TAS Action'),  # To use as a filter to include in incidences
        ],
        string='Type',
        default="consu",
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges