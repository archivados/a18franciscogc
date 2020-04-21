# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class IncidenceAction(models.Model):
    """Model that describes the actions taken in incidences.
    """

    # Private attributes
    _name = 'xestionsat.incidence.action'
    _inherits = {'product.template': 'template_id'}
    _order = 'date_start desc'

    # Default methods

    # Fields declaration
    # Relational Fields
    executed_by = fields.Many2one(
        'res.users',
        string='Executed_by',
        ondelete='restrict',
        default=lambda self: self.env.user,
        required=True,
    )

    incidence_id = fields.Many2one(
        'xestionsat.incidence',
        ondelete='cascade',
    )
    template_id = fields.Many2one(
        'product.template',
        string='Action',
        ondelete='cascade',
    )

    date_start = fields.Date(
        string='Date start',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d')
    )
    date_end = fields.Date(
        string='Date ends',
    )

    observation = fields.Char(
        string='Observations',
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges
    @api.constrains('executed_by')
    def _check_executed_by(self):
        """Verify that the creation of the action is not assigned to a different system user than the one running the application.
        """
        for actuacion in self:
            if actuacion.executed_by and actuacion.executed_by != self.env.user:
                raise models.ValidationError(_('One user cannot create Actions in the name of another'))