# 1: imports of python lib
from datetime import datetime
from lxml import etree

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class Incidence(models.Model):
    """Model to manage the information of an incidence.
    """
    # Private attributes
    _name = 'xestionsat.incidence'
    _description = _('Incidence associated with a Customer')
    _rec_name = 'title'
    _order = 'date_start desc'

    # Default methods

    # Fields declaration
    # Relational Fields
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        ondelete='restrict',
        required=True,
    )
    device_ids = fields.Many2many(
        'xestionsat.device',
        string='Devices',
        required=True,
    )
    created_by_id = fields.Many2one(
        'res.users',
        string='Created by',
        ondelete='restrict',
        default=lambda self: self.env.user,
        required=True,
    )

    incidence_action_ids = fields.One2many(
        'xestionsat.incidence.action',
        string='Incidence Actions',
        inverse_name='incidence_id',
    )

    date_start = fields.Date(
        string='Date start',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d'),
        required=True,
    )
    date_end = fields.Date(
        string='Date ends',
    )

    state = fields.Many2one(
        'xestionsat.incidence.state',
        string='State',
        required=True,
    )

    assistance_place = fields.Many2one(
        'xestionsat.incidence.assistance_place',
        string='Place of assistance',
    )

    # Other Fields
    title = fields.Char(
        string='Title',
        required=True,
        index=True,
    )
    failure_description = fields.Char(
        string='Description of the failure',
        required=True,
    )
    observation = fields.Char(
        string='Observations',
    )
    state_value = fields.Char(
        string='State Value',
        readonly=True,
        compute='_change_state',
        translate=True,
    )

    # compute and search fields, in the same order that fields declaration
    @api.depends('state')
    def _change_state(self):
        """Apply a change of status.
        :param new_state: New state to be assigned.
        """
        for incidence in self:
            incidence.state_value = incidence.state.state

    # Constraints and onchanges
    @api.constrains('device_ids')
    def _check_father(self):
        """Verify that the devices associated with the incidence belong to the
        customer.
        """
        error_message = 'The Device must belong to the specified Customer'

        for incidencia in self:
            for device in incidencia.device_ids:
                if device and device.owner_id != incidencia.customer_id:
                    raise models.ValidationError(_(error_message))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        """Verify that incidence creation is not assigned to a different
        system user than the one running the application.
        """
        error_message = 'One User cannot create Incidences in the name of' \
            'another'

        for incidencia in self:
            if incidencia.created_by_id \
                    and incidencia.created_by_id != self.env.user:
                raise models.ValidationError(_(error_message))

    # CRUD methods
    @api.multi
    def create_new_incidence(
        self, name='New incidence', context=None, flags=None
    ):
        """Method to create a new incidence according to the past context.
        """
        return {
            'name': _(name),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.incidence',
            'view_type': 'form',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'flags': flags,
        }

    # Action methods
    @api.multi
    def add_action(self):
        """Method to add a new action for the current incidence.
        """
        context = {
            'lock_view': True,
            'default_incidence_id': self.id,
        }

        flags = {
            'action_buttons': True,
        }

        return self.env['xestionsat.incidence.action'].create_new_action(
            context=context, flags=flags)

    @api.multi
    def create_order(self):
        """Method to create a new order for the current incidence.
        """
        """
        line_env = self.env['sale.order.line']
        for wizard in self:
            for what in wizard.entries:
                new_line = line_env.create({
                            'product_id': what.product_id.id,
                            'name': what.product_id.name,
                            'order_id': what.sale_order_id.id,
                            'product_uom' : what.product_id.uom_id.id})                
                new_line.product_id_change() #Calling an onchange method to update the record
        """
        return self.create_order_modify()

    @api.multi
    def create_order_modify(
        self, name='Create Order and modify it', context=None, flags=None
    ):
        """Method to create a new order for the current incidence and modify it.
        """
        order_line = []

        for line in self.incidence_action_ids:
            order_line.append(line.prepare_order_line())

        partner = self.customer_id.id
        context = {
            'default_partner_id': partner,
            'default_order_line': order_line,
            'default_picking_policy': 'direct',
        }

        flags = {
            'action_buttons': True,
        }

        return {
            'name': _(name),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_type': 'form',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'flags': flags,
        }

    # Business methods
    @api.model
    def fields_view_get(self, view_id=None, view_type=None, **kwargs):
        """Modify the resulting view according to the past context.
        """
        context = self.env.context

        result = super(Incidence, self).fields_view_get(
            view_id=view_id, view_type=view_type, **kwargs
        )

        if view_type == 'form':
            lock = False

            if 'lock_view' in context:
                lock = context['lock_view']

            if lock:
                doc = etree.XML(result['arch'])

                # Form
                for node in doc.xpath("//form[@name='primary_form']"):
                    node.set('create', 'false')
                    node.set('edit', 'false')

                # customer_id
                for node in doc.xpath("//field[@name='customer_id']"):
                    node.set('modifiers', '{"readonly": true}')

                # btn_add_action
                for node in doc.xpath("//button[@name='add_action']"):
                    node.set('modifiers', '{"invisible": true}')

                # btn_close
                for node in doc.xpath("//button[@name='btn_close']"):
                    node.set('modifiers', '{}')

                result['arch'] = etree.tostring(doc)
        return result
