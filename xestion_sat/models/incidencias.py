# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api

class Incidencias(models.Model):
    ### Campos modelo
    _name = 'xestionsat.incidencias'
    _description = 'XestionSAT Incidencias'
    _order = 'data_ini desc'
    
    ### Campos relacionados
    partner_id = fields.Many2one('res.partner', string='Cliente', ondelete='restrict', required=True)
    equipos_ids = fields.Many2many('xestionsat.equipos', string='Equipos', required=True)
    creado_id = fields.Many2one('res.partner', string='Creado por', ondelete='restrict', required=True)

    actuacionsincidencia_ids = fields.One2many('xestionsat.actuacionsincidencia', inverse_name='incidencias_id')

    data_ini = fields.Date('Data de Incio', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_fin = fields.Date('Data de Finalización')

    estado = fields.Many2one('xestionsat.estadosincidencia', string='Estado')

    lugar = fields.Many2one('xestionsat.lugaresincidencia', string='Lugar de asistencia')

    ### Campos propios
    titulo = fields.Char('Título', required=True)
    descricion = fields.Char('Descrición do cliente', required=True)
    observacions = fields.Char('Observacións')

class EstadosIncidencia(models.Model):
    ### Campos modelo
    _name = 'xestionsat.estadosincidencia'
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
    _description = 'XestionSAT Lugares Incidencia'

    ### Campos propios
    lugar = fields.Char('Lugar', required=True)
    descricion = fields.Char('Descrición')

class ActuacionsIncidencia(models.Model):
    ### Campos modelo
    _name = 'xestionsat.actuacionsincidencia'
    _description = 'XestionSAT Actuacións Incidencia'
    _order = 'data_ini desc'

    ### Campos relacionados
    executado_id = fields.Many2one('res.partner', string='Executada por', ondelete='restrict', required=True)

    incidencias_id = fields.Many2one('xestionsat.incidencias', ondelete='cascade')
    template_id = fields.Many2one('product.template', ondelete='cascade')

    ### Campos propios
    data_ini = fields.Date('Data de Incio', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_fin = fields.Date('Data de Finalización')

    observacions = fields.Char('Observacións')

#class Accions(models.Model):
#    ### Campos modelo
#    _name = 'xestionsat.actuacions'
#    _inherits = {'product.template': 'template_id'}
#    _description = 'XestionSAT Accións Incidencia'

#    template_id = fields.Many2one('product.template', ondelete='cascade')
#    nome = fields.Char('Nome descriptivo', required=True)
