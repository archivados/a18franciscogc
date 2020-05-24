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
    highlight = fields.Selection(
        selection=[
            ('normal', 'Normal'),
            ('decoration-bf', 'Bold'),
            ('decoration-it', 'Italics'),
            ('decoration-danger', 'Light Red'),
            ('decoration-info', 'Light Blue'),
            ('decoration-muted', 'Light Gray'),
            ('decoration-primary', 'Light Purple'),
            ('decoration-success', 'Light Green'),
            ('decoration-warning', 'Light Brown'),
        ],
        string='Highlight',
        default='normal',
        required=True,
    )
    fold = fields.Boolean(
        string='Folded in Pipeline'
    )
    lock_incidence = fields.Boolean(
        string='Lock the Incidence'
    )
    cancel_incidence = fields.Boolean(
        string='Cancel the Incidence'
    )
