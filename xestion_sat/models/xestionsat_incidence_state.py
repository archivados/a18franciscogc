# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class IncidenceState(models.Model):
    # Private attributes
    _name = 'xestionsat.incidence.state'
    _rec_name = 'state'
    _order = "sequence, state, id"

    # Default methods

    # Fields declaration
    # Relational Fields

    # Other Fields
    state = fields.Char(
        string='State',
        translate=True,
        required=True,
    )
    sequence = fields.Integer(
        string='Sequence',
        default=1,
    )
    description = fields.Char(
        string='Description',
        translate=True,
    )