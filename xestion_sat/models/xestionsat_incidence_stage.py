# 1: imports of python lib

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class IncidenceStage(models.Model):
    """Model that describes the stages of an incidence.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _name = 'xestionsat.incidence.stage'
    _description = _('Stage in which an incidence is found')
    _rec_name = 'stage'
    _order = "sequence, stage, id"

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Other Fields
    # -------------------------------------------------------------------------
    stage = fields.Char(
        string='Stage',
        translate=True,
        required=True,
    )
    sequence = fields.Integer(
        string='Sequence',
        default=1,
        required=True,
    )
    description = fields.Text(
        string='Description',
        translate=True,
    )
    fold = fields.Boolean('Folded in Pipeline')
