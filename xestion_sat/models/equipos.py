# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api

class Equipos(models.Model):
    ### Campos modelo
    _name = 'xestionsat.equipos'
    _description = 'XestionSAT Equipos'
    _order = 'cliente_id, nome'
    
    ### Campos relacionados
    cliente_id = fields.Many2one('res.partner', string='Cliente', ondelete='cascade', required=True)
    sede_id = fields.Many2one('res.partner', 
        string='Dirección sede', 
        #domain=[('parent_id', '=', 'cliente_id')],
        ondelete='restrict', 
        required=True)
        
    usuarios_ids = fields.Many2many('res.partner', string='Usuarios')

    componhentesequipo_ids = fields.One2many('xestionsat.componhentesequipo', inverse_name='equipo_id')

    ### Campos propios
    data_alta = fields.Date('Data de Alta', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_baixa = fields.Date('Data de Baixa')

    estado = fields.Selection([
        ('almacenado', 'Almacenado'),
        ('operativo', 'Operativo'),
        ('reparandose', 'Reparandose'),
        ('baixa', 'Baixa')],
        'Estado', default="operativo", required=True)

    nome = fields.Char('Nome', required=True)
    ubicacion = fields.Char('Ubicación')
    descricion = fields.Char('Descrición')
    observacions = fields.Char('Observacións')

    ### Restriccións

class ComponhentesEquipo(models.Model):
    ### Campos modelo
    _name = 'xestionsat.componhentesequipo'
    _inherits = {'product.template': 'template_id'}
    _description = 'XestionSAT Compoñentes Equipo'

    ### Campos relacionados
    template_id = fields.Many2one('product.template', string='Compoñente', ondelete='cascade', required=True)
    equipo_id = fields.Many2one('xestionsat.equipos', string='ID Equipo', ondelete='cascade', required=True)

    ### Campos propios
    #nome = fields.Char('Nome descriptivo', required=True)
    serial = fields.Char('Número de serie')
    observacions = fields.Char('Observacións')
