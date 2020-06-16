# 1: imports of python lib
from lxml import etree

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules
from .xestionsat_common import compare_list, message_post_list

from .xestionsat_common import NEW_INCIDENCE
from .xestionsat_common import ORDER_MODEL, INVOICE_MODEL
from .xestionsat_common import CREATE_ORDER, CREATE_INVOICE
from .xestionsat_common import COLOR_KANBAN_STATE, STATE_DEVICE

from .xestionsat_message import MESSAGE

# 5: local imports

# 6: Import of unknown third party lib


class Incidence(models.Model):
    """Model to manage the information of an incidence.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _name = 'xestionsat.incidence'
    _description = _('Incidence')
    _rec_name = 'title'
    _order = 'id desc, date_start desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

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

    @api.model
    def _get_kanban_stage_items(self):
        """ Get the values for the kanban_stage.
        """
        items = []

        for key, value in COLOR_KANBAN_STATE.items():
            items.append(
                (key, _(value[0]))
            )
        return items

    @api.model
    def _get_default_kanban_state(self):
        """ Gives default kanban_stage.
        """
        default = list(COLOR_KANBAN_STATE.keys())[0]
        return default

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Relational Fields
    # -------------------------------------------------------------------------
    invoice_id = fields.Many2many(
        'account.invoice',
        string='Incidence',
        copy=False,
    )
    sale_order_id = fields.Many2many(
        'sale.order',
        string='Incidence',
        copy=False,
    )

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
        copy=False,
    )

    created_by_id = fields.Many2one(
        'res.users',
        string='Created by',
        ondelete='restrict',
        default=lambda self: self.env.user,
        required=True,
        copy=False,
        track_visibility=True,
    )

    incidence_action_ids = fields.One2many(
        'xestionsat.incidence.action',
        string='Incidence Actions',
        inverse_name='incidence_id',
        copy=False,
        track_visibility=True,
    )

    stage_id = fields.Many2one(
        'xestionsat.incidence.stage',
        string='Stage',
        required=True,
        ondelete='restrict',
        index=True,
        default=_get_default_stage_id,
        group_expand='_get_all_stage_ids',
        copy=False,
        track_visibility=True,
    )

    stage_value = fields.Char(
        readonly=True,
        related='stage_id.stage',
    )

    assistance_place = fields.Many2one(
        'xestionsat.incidence.assistance_place',
        string='Place of assistance',
        ondelete='restrict',
        default=_get_default_place,
        required=True,
        track_visibility=True,
    )

    # -------------------------------------------------------------------------
    # Other Fields
    # -------------------------------------------------------------------------
    title = fields.Char(
        string='Title',
        required=True,
        index=True,
        track_visibility=True,
    )
    failure_description = fields.Text(
        string='Description of the failure',
        required=True,
    )
    observation = fields.Text(
        string='Observations',
        track_visibility=True,
    )

    date_start = fields.Datetime(
        string='Date start',
        default=lambda *a: fields.Datetime.now(),
        required=True,
        track_visibility=True,
    )
    date_end = fields.Datetime(
        string='Date ends',
        copy=False,
        track_visibility=True,
    )

    # Economic Summary
    company_currency = fields.Many2one(
        string='Currency',
        related='company_id.currency_id',
        readonly=True,
        relation="res.currency"
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        index=True,
        default=lambda self: self.env.user.company_id.id
    )

    tax_amount = fields.Monetary(
        string='Tax amount',
        compute='_compute_incidence_action_ids',
        currency_field='company_currency',
        store=True,
        copy=False,
    )
    total_discount = fields.Monetary(
        string='Total discount',
        compute='_compute_incidence_action_ids',
        currency_field='company_currency',
        copy=False,
        store=True,
    )
    total = fields.Monetary(
        string='Untaxed Amount',
        compute='_compute_incidence_action_ids',
        currency_field='company_currency',
        store=True,
        copy=False,
    )
    total_tax = fields.Monetary(
        string='Total',
        compute='_compute_incidence_action_ids',
        currency_field='company_currency',
        store=True,
        copy=False,
    )

    # Summary of actions
    number_total_actions = fields.Integer(
        string='Actions',
        store=True,
        compute='_compute_incidence_action_ids',
    )
    number_open_actions = fields.Integer(
        string='Open Actions',
        store=True,
        compute='_compute_incidence_action_ids',
    )
    number_actions = fields.Char(
        string='Actions',
        readonly=True,
        compute='_compute_incidence_action_ids',
    )

    # Blocking flags
    invoiced = fields.Boolean(
        copy=False,
    )
    locked = fields.Boolean(
        copy=False,
    )

    # Kanban control
    color = fields.Integer(
        string='Color Index',
        # compute='_change_color',
        default=0,
    )
    priority = fields.Selection(
        selection=[
            ('0', _('Low')),
            ('1', _('Normal')),
            ('2', _('High')),
        ],
        string='Priority',
        default='1',
        track_visibility=True,
    )
    kanban_state = fields.Selection(
        selection=_get_kanban_stage_items,
        string='Kanban State',
        default=_get_default_kanban_state,
        copy=False,
        track_visibility=True,
    )

    ###########################################################################
    # compute and search fields, in the same order that fields declaration
    ###########################################################################
    @api.depends('incidence_action_ids')
    def _compute_incidence_action_ids(self):
        """Method to obtain the total price of the action lines and to obtain
        the total number of actions related to the incidence.
        """
        for record in self:
            record.number_total_actions = len(record.incidence_action_ids)
            record.number_open_actions = 0

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

            if record.number_total_actions > 0:
                for action in record.incidence_action_ids:
                    if not action.date_end:
                        record.number_open_actions += 1
            record.number_actions = "{0} ({1})".format(
                record.number_total_actions, record.number_open_actions)

    ###########################################################################
    # Constraints and onchanges
    ###########################################################################

    # -------------------------------------------------------------------------
    # constrains
    # -------------------------------------------------------------------------
    @api.constrains('device_ids')
    def _check_parent(self):
        """Verify that the devices associated with the incidence belong to the
        customer.
        """
        for record in self:
            for device in record.device_ids:
                if device and device.owner_id != record.customer_id:
                    raise models.ValidationError(
                        _(MESSAGE['incidence_constraint']['parent']))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        """Verify that incidence creation is not assigned to a different
        system user than the one running the application.
        """
        for record in self:
            if record.created_by_id \
                    and record.created_by_id != self.env.user:
                raise models.ValidationError(
                    _(MESSAGE['incidence_constraint']['created_by_id']))

    @api.constrains('date_start', 'date_end')
    def _check_date_end(self):
        """Check that the end date is not earlier than the start date.
        """
        self._check_number_actions
        for record in self:
            if record.date_end:
                if record.date_end < record.date_start:
                    raise models.ValidationError(
                        _(MESSAGE['incidence_constraint']['date_end']))
                if record.number_open_actions > 0:
                    raise models.ValidationError(
                        _(MESSAGE['incidence_error']['date_end']).format(
                            record.number_open_actions))

    @api.constrains('invoiced')
    def _compute_invoice(self):
        for record in self:
            if record.sale_order_id or record.invoice_id:
                raise models.ValidationError(
                    _(MESSAGE['incidence_constraint']['invoiced']))

    # -------------------------------------------------------------------------
    # Onchange
    # -------------------------------------------------------------------------
    @api.onchange('stage_id')
    def _check_stage_id(self):
        """Check the current stage_id.
        """
        # It will be changed to the one indicated in the settings
        # (coming soon)
        final_stage = self.env['xestionsat.incidence.stage'].search(
            [('sequence', '=', 6)])

        if self.stage_id == final_stage:
            self.stage_id = None

    @api.onchange('device_ids')
    def _check_device_ids(self):
        """Check the status of the device_ids.
        """
        for device_id in self.device_ids:
            incidences = device_id.get_active_incidence()
            if len(incidences) > 0:
                if self._origin.id not in incidences:
                    raise models.ValidationError(
                        _(MESSAGE['device_constraint']['in_active_incidence']))
            device_id.state = STATE_DEVICE[1][0]

            device_msg = '<li>Add to Incidence: {0} - {1}</li>'.format(
                self.id, self.title)

            device_id.message_post(body='<ul>' + _(device_msg) + '</ul>')

    ###########################################################################
    # CRUD methods
    ###########################################################################
    @api.multi
    def write(self, vals):
        if 'invoiced' not in vals:
            if 'locked' not in vals:
                if self.locked:
                    raise models.ValidationError(
                        _(MESSAGE['incidence_error']['locked']))
            if 'stage_id' in vals:
                if not vals['stage_id']:
                    raise models.ValidationError(
                        _(MESSAGE['incidence_error']['close']))

        if 'device_ids' in vals:
            # Devices Tracking
            old_devices = self.device_ids
            devices_msg = ''

            if len(old_devices) > 0:
                devices_msg += '<b>Old Devices</b><ul>'
                for device in old_devices:
                    devices_msg += message_post_list(
                        {
                            'ID:': device.internal_id,
                            'Name:': device.name,
                            'Location:': device.location,
                            'Headquarter:': device.headquarter_id.display_name,
                        }
                    )

        if 'incidence_action_ids' in vals:
            # Actions Tracking
            old_actions = self.incidence_action_ids
            actions_msg = ''

            if len(old_actions) > 0:
                actions_msg += '<b>Old Actions</b><ul>'
                for action in old_actions:
                    actions_msg += message_post_list(
                        {
                            'Executed by:': action.executed_by.display_name,
                            'Action:': action.product_id.display_name,
                            'Start Date:': action.date_start,
                            'End Date:': action.date_end,
                        }
                    )

        super(Incidence, self).write(vals)

        # Devices Tracking
        if 'device_ids' in vals:
            if not compare_list(old_devices, self.device_ids):
                devices_msg += '</ul><b>New Devices</b><ul>'

                for device in self.device_ids:
                    devices_msg += message_post_list(
                        {
                            'ID:': device.internal_id,
                            'Name:': device.name,
                            'Location:': device.location,
                            'Headquarter:': device.headquarter_id.display_name,
                        }
                    )

                self.message_post(body=_(devices_msg) + '</ul>')

        # Actions Tracking
        if 'incidence_action_ids' in vals:
            if not compare_list(old_actions, self.incidence_action_ids):
                actions_msg += '</ul><b>New Actions</b><ul>'

                for action in self.incidence_action_ids:
                    actions_msg += message_post_list(
                        {
                            'Executed by:': action.executed_by.display_name,
                            'Action:': action.product_id.display_name,
                            'Start Date:': action.date_start,
                            'End Date:': action.date_end,
                        }
                    )

                self.message_post(body=_(actions_msg) + '</ul>')

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

        if self.invoiced or self.locked:
            raise models.UserError(
                _(MESSAGE['incidence_methods']['add_action']))
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
    def close_incidence(self):
        """Method to close or reopen the current Incidence.
        """
        message_post = ''

        # It will be changed to the one indicated in the settings
        # (coming soon)
        final_stage = self.env['xestionsat.incidence.stage'].search(
            [('sequence', '=', 6)])
        wait_stage = self.env['xestionsat.incidence.stage'].search(
            [('sequence', '=', 3)])

        # Restrictions not to edit this field are assumed to work
        self.invoiced = False
        self._compute_incidence_action_ids()
        date_now = False

        # All devices should have the same status
        devices_state = STATE_DEVICE[1][0]

        next_stage = self.stage_id \
            if self.stage_id != final_stage else wait_stage

        # If the record is locked it unlocks it so you can write the changes
        if self.locked:
            self.locked = False
            lock = False
        else:
            lock = True

        if not self.date_end:
            date_now = fields.Datetime.now()
            next_stage = final_stage
            devices_state = STATE_DEVICE[0][0]

        self.date_end = date_now
        self.stage_id = next_stage
        for record in self.device_ids:
            record.state = devices_state

        # It is the last value to change so as not to block the other changes
        self.locked = lock

        if self.locked:
            message_post = 'Incidence closed'
        else:
            message_post = 'Open incidence'

        self.message_post(body='<ul><li>' + _(message_post) + '</li></ul>')

    # -------------------------------------------------------------------------
    # Order actions
    # -------------------------------------------------------------------------
    def create_batch_order(self, records):
        """Method to create a new order for a set of incidences.

        :param records: Records to work on.
        """
        return self._get_invoice_order(
            ORDER_MODEL, CREATE_ORDER, records, False)

    @api.multi
    def create_order(self):
        """Method to create a new order for the current incidence.

        :param show_message: Indicates whether or not to display a message to
        the user.
        """
        return self._get_invoice_order(
            ORDER_MODEL, CREATE_ORDER, self, True)

    @api.multi
    def create_order_edit(self, name=CREATE_ORDER):
        """Method to create a new order for the current incidence and modify it.

        :param name: View title.
        """
        if type(name) != str:
            name = CREATE_ORDER

        # pricelist_id = self.env['product.pricelist'].search([], limit=1).id

        context = {
            'default_incidence_ids': [self.id],
            'default_partner_id': self.customer_id.id,
            'default_order_line': self._get_actions_lines(ORDER_MODEL, self),
            # 'default_confirmation_date': fields.Datetime.now(),
            # 'default_pricelist_id': pricelist_id,
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
    def create_batch_invoice(self, records):
        """Method to create a new order for a set of incidences.

        :param records: Records to work on.
        """
        return self._get_invoice_order(
            INVOICE_MODEL, CREATE_INVOICE, records, False)

    @api.multi
    def create_invoice(self):
        """Method to create a new invoice for the current incidence.

        :param show_message: Indicates whether or not to display a message to
        the user.
        """
        return self._get_invoice_order(
            INVOICE_MODEL, CREATE_INVOICE, self, True)

    @api.multi
    def create_invoice_edit(self, name=CREATE_INVOICE):
        """Method to create a new invoice for the current incidence and modify it.

        :param name: View title.
        """
        if type(name) != str:
            name = CREATE_INVOICE

        context = {
            'default_incidence_ids': [self.id],
            'default_partner_id': self.customer_id.id,
            'default_invoice_line_ids': self._get_actions_lines(
                INVOICE_MODEL, self),
        }

        flags = {
            'action_buttons': True,
        }

        return self._get_invoice_order_view(
            INVOICE_MODEL, name, context, flags)

    # -------------------------------------------------------------------------
    # Common actions for Orders and Invoices
    # -------------------------------------------------------------------------
    def _prepare_batch_records(self, return_model, records):
        """Method to create a new order for a set of incidences.

        :param records: Records to work on.
        """
        orders = dict()

        for item in records:
            if item.invoiced:
                continue

            if item.customer_id.id not in orders:
                orders[item.customer_id.id] = ([], [])

            items = item._get_actions_lines(return_model, item)
            # Incidence Actions
            orders[item.customer_id.id][0].extend(items)
            # Incidences (to mark as invoiced)
            orders[item.customer_id.id][1].extend(item)

        return orders

    def _get_actions_lines(self, res_model, record):
        """Method to obtain the lines of action related to the incidence.

        :param res_model: Model for which it is generated.
        :param record: Record to work on.
        """
        lines = []

        lines.append((
            0, 0,
            {
                'name': '(' + record.date_start.strftime("%Y-%m-%d") + ' - '
                + record.date_start.strftime("%Y-%m-%d")
                + ') Incidence: ' + record.title,
                'display_type': 'line_section',
            },
        ))
        for line in record.incidence_action_ids:
            lines.append(line.prepare_action_line(res_model))

        return lines

    def _get_invoice_order(
        self, return_model, title_message, records, show_message
    ):
        """Method that generates an order or an invoice without user intervention.

        :param res_model: Model to generate.
        :param title_message: Reply message title.
        :param show_message: Indicates whether or not to display a message to
        the user.
        """
        lines_type = ''
        state = ''
        message_post = ''

        orders = self._prepare_batch_records(return_model, records)

        if return_model == ORDER_MODEL:
            lines_type = 'order_line'
            state = 'sale'
            msg_type = 'Order'

        if return_model == INVOICE_MODEL:
            lines_type = 'invoice_line_ids'
            state = 'draft'
            msg_type = 'Invoice'

        if len(orders) > 0:
            try:
                for customer, items in orders.items():
                    # Mark Incidences as invoiced and past ids for the model
                    incidences = []

                    for incidence in items[1]:
                        incidence.invoiced = True
                        incidences.append(incidence.id)

                    model = self.env[return_model].create({
                        'partner_id': customer,
                        lines_type: items[0],
                        'state': state,
                    })

                    if return_model == ORDER_MODEL:
                        model['confirmation_date'] = fields.Datetime.now()

                    model['incidence_ids'] = incidences

                    if show_message:
                        message_id = self.env['xestionsat.message'].create(
                            {
                                'message': _(
                                    MESSAGE['incidence_methods']
                                    ['_get_invoice_order'])
                            }
                        )

                        if self.invoiced:
                            message_post = msg_type + ' created'

                        self.message_post(
                            body='<ul><li>' + _(message_post) + '</li></ul>')

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
                raise models.UserError(
                    _(MESSAGE['incidence_error']['operation']) + str(e))

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
        self.invoiced = True
        message_post = ''

        if res_model == ORDER_MODEL:
            msg_type = 'Order'

        if res_model == INVOICE_MODEL:
            msg_type = 'Invoice'

        if self.invoiced:
            message_post = msg_type + ' windows open'

        self.message_post(body='<ul><li>' + _(message_post) + '</li></ul>')

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
        """Modify the resulting view according to user preferences.
        """
        context = self.env.context

        result = super(Incidence, self).fields_view_get(
            view_id=view_id, view_type=view_type, **kwargs
        )

        doc = etree.XML(result['arch'])

        if view_type == 'form':
            lock = False

            try:
                record = self.env['xestionsat.incidence'].browse(
                    self._context.get('params').get('id'))

                locked = record.locked
            except Exception:
                locked = False

            if 'lock_view' in context:
                lock = context['lock_view']

            if lock or locked:
                # Form
                for node in doc.xpath("//form[@name='primary_form']"):
                    if not locked:
                        node.set('create', 'false')

                    node.set('edit', 'false')

                # customer_id
                for node in doc.xpath("//field[@name='customer_id']"):
                    node.set('modifiers', '{"readonly": true}')

                # btn_add_action
                for node in doc.xpath("//button[@name='add_action']"):
                    node.set('modifiers', '{"invisible": true}')

                # btn_close
                if not locked:
                    for node in doc.xpath("//button[@name='btn_close']"):
                        node.set('modifiers', '{}')

        if view_type == 'tree':
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

        if view_type == 'kanban':
            # kanban
            for node in doc.xpath("//progressbar[@field='kanban_state']"):
                colors = '{'

                # A comma after the last dictionary element causes an error
                # when creating the view
                number_values = len(COLOR_KANBAN_STATE.values())
                i = 1
                for color, state in COLOR_KANBAN_STATE.items():
                    if color != 'none':
                        colors += '"' + color + '": "' + state[1] + '"'

                        if i < number_values:
                            colors += ', '
                    i += 1

                colors += '}'
                node.set('colors', colors)

        result['arch'] = etree.tostring(doc)

        return result
