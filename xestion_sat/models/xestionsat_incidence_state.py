# 1: imports of python lib

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class IncidenceState(models.Model):
    """Model that describes the states of an incidence.
    """
    # Private attributes
    _name = 'xestionsat.incidence.state'
    _description = _('State in which an incidence is found')
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
        required=True,
    )
    description = fields.Char(
        string='Description',
        translate=True,
    )
