# 1: imports of python lib
from lxml import etree

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules
from .xestionsat_common import NEW_INCIDENCE
from .xestionsat_common import ORDER_MODEL, INVOICE_MODEL
from .xestionsat_common import CREATE_ORDER, CREATE_INVOICE

# 5: local imports

# 6: Import of unknown third party lib


class Incidence(models.Model):
    """Model to manage the information of an incidence.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _name = 'xestionsat.incidence'
    _description = _('Incidence associated with a Customer')
    _rec_name = 'title'
    _order = 'id desc, date_start desc'

    ###########################################################################
    # Default methods
    ###########################################################################
    @api.model
    def _get_default_place(self):
        """ Gives default assistance_place.
        """
        places = self.env['xestionsat.incidence.assistance_place'].search([])

        return places[0] if places else False

    @api.model
    def _get_default_stage_id(self):
        """ Gives default stage_id.
        """
        stage_ids = self.env['xestionsat.incidence.stage'].search([])

        return stage_ids[0] if stage_ids else False

    @api.model
    def _get_all_stage_ids(self, stages, domain, order):
        """ Gives all stage_ids.
        """
        return self.env['xestionsat.incidence.stage'].search([])

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Relational Fields
    # -------------------------------------------------------------------------
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
        ondelete='restrict',
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

    stage_id = fields.Many2one(
        'xestionsat.incidence.stage',
        string='Stage',
        required=True,
        ondelete='restrict',
        index=True,
        default=_get_default_stage_id,
        group_expand='_get_all_stage_ids',
    )

    assistance_place = fields.Many2one(
        'xestionsat.incidence.assistance_place',
        string='Place of assistance',
        ondelete='restrict',
        default=_get_default_place,
        required=True,
    )

    # -------------------------------------------------------------------------
    # Other Fields
    # -------------------------------------------------------------------------
    title = fields.Char(
        string='Title',
        required=True,
        index=True,
    )
    failure_description = fields.Text(
        string='Description of the failure',
        required=True,
    )
    observation = fields.Text(
        string='Observations',
    )

    date_start = fields.Datetime(
        string='Date start',
        default=lambda *a: fields.Datetime.now(),
        required=True,
    )
    date_end = fields.Datetime(
        string='Date ends',
    )

    stage_value = fields.Char(
        readonly=True,
        related='stage_id.stage',
        translate=True,
    )

    # Economic Summary
    tax_amount = fields.Float(
        string='Tax amount',
        readonly=True,
        compute='_compute_actions_total',
    )
    total_discount = fields.Float(
        string='Total discount',
        readonly=True,
        compute='_compute_actions_total',
    )
    total = fields.Float(
        string='Untaxed Amount',
        readonly=True,
        compute='_compute_actions_total',
    )
    total_tax = fields.Float(
        string='Total',
        readonly=True,
        compute='_compute_actions_total',
    )

    # Summary of actions
    number_total_actions = fields.Integer(
        string='Open Actions',
        readonly=True,
        compute='_compute_number_actions',
    )
    number_open_actions = fields.Integer(
        string='Actions',
        readonly=True,
        compute='_compute_number_actions',
    )
    number_actions = fields.Char(
        string='Actions',
        readonly=True,
        compute='_compute_number_actions',
    )

    # Blocking flags
    invoiced = fields.Boolean()
    locked = fields.Boolean()

    ###########################################################################
    # compute and search fields, in the same order that fields declaration
    ###########################################################################
    @api.depends('incidence_action_ids')
    def _compute_number_actions(self):
        """Method to obtain the total price of the action lines related to the
        incidence.
        """
        for record in self:
            record.number_total_actions = len(record.incidence_action_ids)
            record.number_open_actions = 0

            if record.number_total_actions > 0:
                for action in record.incidence_action_ids:
                    if not action.date_end:
                        record.number_open_actions += 1
            record.number_actions = "{0} ({1})".format(
                record.number_total_actions, record.number_open_actions)

    @api.depends('incidence_action_ids')
    def _compute_actions_total(self):
        """Method to obtain the total number of actions related to the
        incidence.
        """
        for record in self:
            record.tax_amount = 0.0
            record.total_discount = 0.0
            record.total = 0.0
            record.total_tax = 0.0

            for line in record.incidence_action_ids:
                tax_amount_line = line.tax_amount_line
                subtotal_discount = line.subtotal_discount
                subtotal = line.subtotal
                subtotal_tax = line.subtotal_tax

                if tax_amount_line is not None:
                    record.tax_amount += tax_amount_line
                if subtotal_discount is not None:
                    record.total_discount += subtotal_discount
                if subtotal is not None:
                    record.total += subtotal
                if subtotal_tax is not None:
                    record.total_tax += subtotal_tax

    ###########################################################################
    # Constraints and onchanges
    ###########################################################################
    @api.constrains('device_ids')
    def _check_father(self):
        """Verify that the devices associated with the incidence belong to the
        customer.
        """
        error_message = 'The Device must belong to the specified Customer'

        for record in self:
            for device in record.device_ids:
                if device and device.owner_id != record.customer_id:
                    raise models.ValidationError(_(error_message))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        """Verify that incidence creation is not assigned to a different
        system user than the one running the application.
        """
        error_message = 'One User cannot create Incidences in the name of' \
            'another'

        for record in self:
            if record.created_by_id \
                    and record.created_by_id != self.env.user:
                raise models.ValidationError(_(error_message))

    @api.constrains('date_start', 'date_end')
    def _check_date_end(self):
        """Check that the end date is not earlier than the start date.
        """
        actions_message = 'There are {0} unclosed actions. All actions need' \
            ' to be closed in order to close the Incidence.'

        error_message = 'The end date cannot be earlier than the start date'

        for record in self:
            if record.date_end:
                if record.date_end < record.date_start:
                    raise models.ValidationError(_(error_message))
                if record.number_open_actions > 0:
                    raise models.ValidationError(
                        _(actions_message.format(record.number_open_actions)))

    @api.onchange('stage_id')
    def _check_stage_id(self):
        """Check the current stage_id.
        """
        # It will be changed to the one indicated in the settings
        # (coming soon)
        final_stage = self.env['xestionsat.incidence.stage'].search(
            [('sequence', '=', 6)])

        if self.stage_id == final_stage:
            self.close_incidence()
        elif self.locked:
            self.locked = False
            self.date_end = False

    ###########################################################################
    # CRUD methods
    ###########################################################################
    @api.multi
    def create_new_incidence(
        self, name=NEW_INCIDENCE, context=None, flags=None
    ):
        """Method to create a new incidence according to the past context.

        :param name: View title.
        :param context: Context to present the view data.
        :param flags: Flags to modify the view.
        """
        if type(name) != str:
            name = NEW_INCIDENCE

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

    ###########################################################################
    # Action methods
    ###########################################################################
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
    def close_incidence(self, final_stage=False):
        """Method to close or reopen the current Incidence.
        """
        # It will be changed to the one indicated in the settings
        # (coming soon)
        if not final_stage:
            final_stage = self.env['xestionsat.incidence.stage'].search(
                [('sequence', '=', 6)])
        wait_stage = self.env['xestionsat.incidence.stage'].search(
            [('sequence', '=', 3)])

        date_now = False
        lock = False

        next_stage = self.stage_id \
            if self.stage_id != final_stage else wait_stage

        if not self.date_end:
            date_now = fields.Datetime.now()
            lock = True
            next_stage = final_stage

        self.date_end = date_now
        self.locked = lock
        self.stage_id = next_stage

    def reload_page(self):
        model_obj = self.env['ir.model.data']
        data_id = model_obj._get_id('xestionsat.incidence', 'view_id')
        view_id = model_obj.browse(data_id).res_id
        return {
            'type': 'ir.actions.act_window',
            'name': _('String'),
            'res_model': 'xestionsat.incidence',
            'view_type': 'tree',
            'view_mode': 'form',
            'view_id': view_id,
            'target': 'current',
            'nodestroy': True,
        }

    # -------------------------------------------------------------------------
    # Order actions
    # -------------------------------------------------------------------------
    @api.multi
    def create_order(self):
        """Method to create a new order for the current incidence.
        """
        return self._get_invoice_order(ORDER_MODEL, CREATE_ORDER)

    @api.multi
    def create_order_edit(self, name=CREATE_ORDER):
        """Method to create a new order for the current incidence and modify it.

        :param name: View title.
        """
        if type(name) != str:
            name = CREATE_ORDER

        # pricelist_id = self.env['product.pricelist'].search(
        #    [], limit=1, order='id desc')

        context = {
            'default_partner_id': self.customer_id.id,
            'default_order_line': self._get_actions_lines(ORDER_MODEL),
            # 'default_confirmation_date': datetime.today(),
            # 'default_pricelist_id': pricelist_id.id,
            # 'default_state': 'sale',
        }

        flags = {
            'action_buttons': True,
        }

        return self._get_invoice_order_view(
            ORDER_MODEL, name, context, flags)

    # -------------------------------------------------------------------------
    # Invoice actions
    # -------------------------------------------------------------------------
    @api.multi
    def create_invoice(self):
        """Method to create a new invoice for the current incidence.
        """
        return self._get_invoice_order(INVOICE_MODEL, CREATE_INVOICE)

    @api.multi
    def create_invoice_edit(self, name=CREATE_INVOICE):
        """Method to create a new invoice for the current incidence and modify it.
        """
        if type(name) != str:
            name = CREATE_INVOICE

        context = {
            'default_partner_id': self.customer_id.id,
            'default_invoice_line_ids': self._get_actions_lines(INVOICE_MODEL),
        }

        flags = {
            'action_buttons': True,
        }

        return self._get_invoice_order_view(
            INVOICE_MODEL, name, context, flags)

    # -------------------------------------------------------------------------
    # Common actions for Orders and Invoices
    # -------------------------------------------------------------------------
    def _get_actions_lines(self, res_model):
        """Method to obtain the lines of action related to the incidence.

        :param res_model: Model for which it is generated.
        """
        lines = []
        for line in self.incidence_action_ids:
            lines.append(line.prepare_action_line(res_model))

        return lines

    def _get_invoice_order(self, return_model, title_message):
        """Method that generates an order or an invoice without user intervention.

        :param res_model: Model to generate.
        :param title_message: Reply message title.
        """
        error_message = 'An error has occurred and the operation could not' \
            ' be completed:\n\n'
        message = 'Automatic process completed, please check that the result' \
            ' is correct.'

        lines_type = ''
        state = ''

        if return_model == ORDER_MODEL:
            lines_type = 'order_line'
            state = 'sale'

        if return_model == INVOICE_MODEL:
            lines_type = 'invoice_line_ids'
            state = 'draft'

        try:
            model = self.env[return_model].create({
                'partner_id': self.customer_id.id,
                lines_type: self._get_actions_lines(return_model),
                'state': state,
            })

            if return_model == ORDER_MODEL:
                model['confirmation_date'] = fields.Datetime.now()

            message_id = self.env['xestionsat.message'].create(
                {'message': _(message)})
            return {
                'name': _(title_message),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'xestionsat.message',
                # pass the id
                'res_id': message_id.id,
                'target': 'new'
            }
        except Exception as e:
            raise models.UserError(_(error_message + str(e)))

    def _get_invoice_order_view(
        self, res_model, name, context=None, flags=None
    ):
        """Method that generates the basis of an order or an invoice and shows
        it to the user for confirmation.

        :param res_model: Model to generate.
        :param name: View title.
        :param context: Context to present the view data.
        :param flags: Flags to modify the view.
        """
        return {
            'name': _(name),
            'type': 'ir.actions.act_window',
            'res_model': res_model,
            'view_type': 'form',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'flags': flags,
        }

    ###########################################################################
    # Business methods
    ###########################################################################
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
        if view_type == 'tree':
            doc = etree.XML(result['arch'])
            stages = dict()

            # Prepare the conditions to change the colors of each row
            for stage in self.env['xestionsat.incidence.stage'].search([]):
                if stage.highlight != 'normal':
                    if stage.highlight in stages:
                        stages[stage.highlight].append(stage.stage)
                    else:
                        stages[stage.highlight] = [stage.stage]

            # Tree
            for node in doc.xpath("//tree[@name='primary_tree']"):
                for decoration, values in stages.items():
                    condition = "stage_value in ("
                    for stage in values:
                        condition += "'" + stage + "', "
                    condition += ")"

                    node.set(decoration, condition)

            result['arch'] = etree.tostring(doc)

        return result
