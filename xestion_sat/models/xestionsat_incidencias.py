# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api

class XestionsatIncidencias(models.Model):
    _name = 'xestionsat.incidencias'
    _description = 'XestionSAT Incidencias'
    _order = 'data_ini desc'
    
    partner_id = fields.Many2one('res.partner', string='Cliente', ondelete='restrict')
    equipos_ids = fields.Many2many('xestionsat.equipos', string='Equipos')
    creado_id = fields.Many2one('res.partner', string='Creado por', ondelete='restrict')

    actuacionsincidencia_ids = fields.One2many('xestionsat.actuacionsincidencia', inverse_name='incidencias_id')

    data_ini = fields.Date('Data de Incio', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_fin = fields.Date('Data de Finalización')

    estado = fields.Many2many('xestionsat.estadosincidencia', 'estadosincidencia', string='Estados')

    lugar = fields.Selection([
        ('taller', 'Taller'),
        ('insitu', 'In Situ Cliente (sede)'),
        ('desprazado', 'In Situ Cliente (desprazado)')],
        'Lugar asistencia', default="taller")

    titulo = fields.Char('Título', required=True)
    descricion = fields.Char('Descrición do cliente', required=True)
    observacions = fields.Char('Observacións')

class XestionsatEstadosIncidencia(models.Model):
    _name = 'xestionsat.estadosincidencia'
    _description = 'XestionSAT Estados Incidencia'

    estado = fields.Char('Estado', required=True)
    descricion = fields.Char('Descrición do cliente', required=True)

    '''
    Posibles estados:
        Pendente
        Iniciada
        En espera
        Enviado a SAT externo
        Recibido
        Finalizada
        Cancelada
        Irreparable
    '''

class XestionsatActuacionsIncidencia(models.Model):
    _name = 'xestionsat.actuacionsincidencia'
    _description = 'XestionSAT Actuacións Incidencia'
    _order = 'data_ini desc'

    executado_id = fields.Many2one('res.partner', string='Executada por', ondelete='restrict')

    incidencias_id = fields.Many2one('xestionsat.incidencias', ondelete='cascade')
    template_id = fields.Many2one('product.template', ondelete='cascade')

    data_ini = fields.Date('Data de Incio', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_fin = fields.Date('Data de Finalización')

    observacions = fields.Char('Observacións')

#class XestionsatAccions(models.Model):
#    _name = 'xestionsat.actuacions'
#    _inherits = {'product.template': 'template_id'}
#    _description = 'XestionSAT Accións Incidencia'

#    template_id = fields.Many2one('product.template', ondelete='cascade')
#    nome = fields.Char('Nome descriptivo', required=True)
