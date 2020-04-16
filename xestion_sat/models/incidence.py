# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class Incidence(models.Model):
    # Private attributes
    _name = 'xestionsat.incidence'
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

    incidenceaction_ids = fields.One2many(
        'xestionsat.incidenceaction',
        string='Incidence Actions',
        inverse_name='incidence_id',
    )

    date_start = fields.Date(
        string='Date start',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d')
    )
    date_end = fields.Date(
        string='Date ends',
    )

    state = fields.Many2one(
        'xestionsat.incidencestate',
        string='State',
    )

    assistance_place = fields.Many2one(
        'xestionsat.incidenceassistanceplace',
        string='Place of assistance',
    )

    # Other Fields
    title = fields.Char(
        string='Title',
        required=True,
    )
    failure_description = fields.Char(
        string='Description of the failure',
        required=True,
    )
    observation = fields.Char(
        string='Observations',
    )
    lock = fields.Boolean(
        string='Lock',
        default=False,
        readonly=True,
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges
    @api.constrains('device_ids')
    def _check_father(self):
        for incidencia in self:
            if incidencia.device_ids and incidencia.device_ids.propietario_id != incidencia.customer_id:
                raise models.ValidationError(_('The Device must belong to the specified customer'))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        for incidencia in self:
            if incidencia.created_by_id and incidencia.created_by_id != self.env.user:
                raise models.ValidationError(_('One user cannot create Incidences in the name of another'))


class IncidenceState(models.Model):
    # Private attributes
    _name = 'xestionsat.incidencestate'
    _rec_name = 'state'

    # Default methods

    # Fields declaration
    # Relational Fields

    # Other Fields
    state = fields.Char(
        string='State',
        required=True,
    )
    description = fields.Char(
        string='Description',
    )

    '''
    Posibles estados:
        Pendente
        Iniciada
        En espera
        Enviado a SAT externo
        Retornado
        Finalizada
        Cancelada
        Irresoluble
    '''


class IncidenceAssistancePlace(models.Model):
    # Private attributes
    _name = 'xestionsat.incidenceassistanceplace'
    _rec_name = 'assistance_place'

    # Default methods

    # Fields declaration
    # Relational Fields
    assistance_place = fields.Char(
        string='Place of assistance',
        required=True,
    )
    description = fields.Char(
        string='Description',
    )

    # Other Fields

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges


class IncidenceAction(models.Model):
    # Private attributes
    _name = 'xestionsat.incidenceaction'
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
        for actuacion in self:
            if actuacion.executed_by and actuacion.executed_by != self.env.user:
                raise models.ValidationError(_('One user cannot create Actions in the name of another'))


class ProductTemplate(models.Model):
    # Private attributes
    _inherit = 'product.template'

    # Default methods

    # Fields declaration
    # Relational Fields
    type = fields.Selection(
        [
            ('consu', 'Consumable'),
            ('service', 'Service'),
            ('sat', 'TAS Action'),
        ],
        string='Type',
        default="consu",
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges