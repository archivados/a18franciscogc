# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class IncidenceAssistancePlace(models.Model):
    """Model that describes the places of assistance of an incidence.
    """

    # Private attributes
    _name = 'xestionsat.incidence.assistance_place'
    _rec_name = 'assistance_place'

    # Default methods

    # Fields declaration
    # Relational Fields
    assistance_place = fields.Char(
        string='Place of assistance',
        translate=True,
        required=True,
    )
    description = fields.Char(
        string='Description',
        translate=True,
    )

    # Other Fields

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges
