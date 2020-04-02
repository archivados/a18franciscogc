# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api

class Incidencias(models.Model):
    ### Campos modelo
    _name = 'xestionsat.incidencias'
    _rec_name = 'titulo'
    _description = 'XestionSAT Incidencias'
    _order = 'data_ini desc'
    
    ### Campos relacionados
    cliente_id = fields.Many2one('res.partner', string='Cliente', ondelete='restrict', required=True)
    equipos_ids = fields.Many2many('xestionsat.equipos', string='Equipos', required=True)
    creado_por_id = fields.Many2one('res.users', string='Creado por', ondelete='restrict', default=lambda self: self.env.user, required=True)

    actuacionsincidencia_ids = fields.One2many('xestionsat.actuacionsincidencia', inverse_name='incidencias_id')

    data_ini = fields.Date('Data de Incio', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_fin = fields.Date('Data de Finalización')

    estado = fields.Many2one('xestionsat.estadosincidencia', string='Estado')

    lugar = fields.Many2one('xestionsat.lugaresincidencia', string='Lugar de asistencia')

    ### Campos propios
    titulo = fields.Char('Título', required=True)
    descricion = fields.Char('Descrición do cliente', required=True)
    observacions = fields.Char('Observacións')
    bloquear = fields.Boolean(default=False, readonly=True)

    ### Restriccións
    @api.constrains ('equipos_ids')
    def _comprobar_pai(self):
        for incidencia in self:
            if incidencia.equipos_ids and incidencia.equipos_ids.propietario_id != incidencia.cliente_id:
                raise models.ValidationError('O Equipo debe pertencer ó cliente especificado')

    @api.constrains ('creado_por_id')
    def _comprobar_creador(self):
        for incidencia in self:
            if incidencia.creado_por_id and incidencia.creado_por_id != self.env.user:
                raise models.ValidationError('Un usuario non pode crear Incidencias no nome de outro')

class EstadosIncidencia(models.Model):
    ### Campos modelo
    _name = 'xestionsat.estadosincidencia'
    _rec_name = 'estado'
    _description = 'XestionSAT Estados Incidencia'

    ### Campos propios
    estado = fields.Char('Estado', required=True)
    descricion = fields.Char('Descrición do etado')

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

class LugaresIncidencia(models.Model):
    ### Campos modelo
    _name = 'xestionsat.lugaresincidencia'
    _rec_name = 'lugar'
    _description = 'XestionSAT Lugares Incidencia'

    ### Campos propios
    lugar = fields.Char('Lugar', required=True)
    descricion = fields.Char('Descrición')

class ActuacionsIncidencia(models.Model):
    ### Campos modelo
    _name = 'xestionsat.actuacionsincidencia'
    _inherits = {'product.template': 'template_id'}
    _description = 'XestionSAT Actuacións Incidencia'
    _order = 'data_ini desc'

    ### Campos relacionados
    executado_por_id = fields.Many2one('res.users', string='Executada por', ondelete='restrict', default=lambda self: self.env.user, required=True)

    incidencias_id = fields.Many2one('xestionsat.incidencias', ondelete='cascade')
    template_id = fields.Many2one('product.template', string='Acción', ondelete='cascade')

    ### Campos propios
    data_ini = fields.Date('Data de Incio', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_fin = fields.Date('Data de Finalización')

    observacions = fields.Char('Observacións')

    ### Restriccións
    @api.constrains ('executado_por_id')
    def _comprobar_creador(self):
        for actuacion in self:
            if actuacion.executado_por_id and actuacion.executado_por_id != self.env.user:
                raise models.ValidationError('Un usuario non pode crear Acccións no nome de outro')

class ProductTemplate(models.Model):
    ### Campos modelo
    _inherit = 'product.template'

    type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service'),
        ('sat', 'Acción de SAT')],
        'Type', default="consu")