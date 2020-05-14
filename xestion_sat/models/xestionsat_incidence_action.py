# 1: imports of python lib
from datetime import datetime
from lxml import etree

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
    _description = _('Action taken in an incidence')
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
        required=True,
        ondelete='cascade',
    )

    date_start = fields.Date(
        string='Date start',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d'),
        required=True,
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
        """Verify that the creation of the action is not assigned to a
        different system user than the one running the application.
        """

        error_message = 'One user cannot create Actions in the name of another'

        for actuacion in self:
            if actuacion.executed_by \
                    and actuacion.executed_by != self.env.user:
                raise models.ValidationError(_(error_message))

    # CRUD methods
    @api.multi
    def create_new_action(
        self, name='Add action', context=None, flags=None
    ):
        """Method to add a new action for the current incidence.
        """

        return {
            'name': _(name),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.incidence.action',
            'view_type': 'form',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'flags': flags,
        }

    # Action methods

    # Business methods
    @api.model
    def fields_view_get(self, view_id=None, view_type=None, **kwargs):
        """Modify the resulting view according to the past context.
        """

        context = self.env.context

        result = super(IncidenceAction, self).fields_view_get(
            view_id=view_id, view_type=view_type, **kwargs
        )

        if view_type == 'form':
            lock = False

            if 'lock_view' in context:
                lock = context['lock_view']

            if lock:
                doc = etree.XML(result['arch'])

                # btn_close
                for node in doc.xpath("//button[@name='btn_close']"):
                    node.set('modifiers', '{}')

                result['arch'] = etree.tostring(doc)
        return result
