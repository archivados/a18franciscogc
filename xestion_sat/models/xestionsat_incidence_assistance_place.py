# 1: imports of python lib

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class IncidenceAssistancePlace(models.Model):
    """Model that describes the places of assistance of an incidence.
    """

    ###########################################################################
    # Private attributes
    ###########################################################################
    _name = 'xestionsat.incidence.assistance_place'
    _description = _('Incidence Assistance Place')
    _rec_name = 'assistance_place'
    _inherit = ['mail.thread']

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Relational Fields
    # -------------------------------------------------------------------------
    assistance_place = fields.Char(
        string='Place of assistance',
        required=True,
        translate=True,
    )
    description = fields.Text(
        string='Description',
        translate=True,
    )
