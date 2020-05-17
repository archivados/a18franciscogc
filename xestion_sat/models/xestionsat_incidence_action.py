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
    # Constants for CRUD messages
    NEW_ACTION = 'Add action'

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

    # Other Fields
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
    quantity = fields.Float(
        string='Quantity',
        default=1.0,
    )
    discount = fields.Float(
        string='Discount (%)',
        inverse='_check_discount',
        default=0.0,
    )
    subtotal = fields.Float(
        string='Subtotal',
        readonly=True,
        compute='_compute_subtotal',
    )

    # compute and search fields, in the same order that fields declaration
    @api.depends('quantity', 'discount', 'list_price')
    def _compute_subtotal(self):
        """Recalculate the price of the line.
        :param new_state: New state to be assigned.
        """
        for line in self:
            unit_discount = line.list_price * line.discount / 100
            unit_price = line.list_price - unit_discount
            line.subtotal = line.quantity * unit_price

    @api.depends('discount')
    def _check_discount(self):
        """Check that the discount is between 1 and 100.
        """
        for line in self:
            if line.discount < 0:
                line.update({
                    'discount': 0,
                })
            elif line.discount > 100:
                line.update({
                    'discount': 100,
                })

    @api.multi
    def prepare_order_line(self):
        """Prepare the dict of values to create the new sales order line.
        """
        self.ensure_one()

        return (0, 0, {
                'name': self.name,
                'product_id': self.id,
                'product_uom_qty': self.quantity,
                'discount': self.discount,
                'product_uom': self.uom_id.id,
                'price_unit': self.list_price, })

    # Constraints and onchanges
    @api.constrains('executed_by')
    def _check_executed_by(self):
        """Verify that the creation of the action is not assigned to a
        different system user than the one running the application.
        """
        error_message = 'One user cannot create Actions in the name of another'

        for line in self:
            if line.executed_by \
                    and line.executed_by != self.env.user:
                raise models.ValidationError(_(error_message))

    # CRUD methods
    @api.multi
    def create_new_action(
        self, name=NEW_ACTION, context=None, flags=None
    ):
        """Method to add a new action for the current incidence.
        """
        if type(name) != str:
            name = self.NEW_ACTION

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
