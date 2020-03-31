# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api

class Equipos(models.Model):
    ### Campos modelo
    _name = 'xestionsat.equipos'
    _rec_name = 'nome'
    _description = 'XestionSAT Equipos'
    _order = 'propietario_id, codigo_interno, nome'
    
    ### Campos relacionados
    creado_por_id = fields.Many2one('res.users', string='Creado por', ondelete='restrict', default=lambda self: self.env.user, required=True)

    propietario_id = fields.Many2one('res.partner', string='Cliente', ondelete='cascade', required=True)
    sede_id = fields.Many2one('res.partner', string='Dirección sede', ondelete='restrict', required=True)
        
    usuarios_ids = fields.Many2many('res.partner', string='Usuarios')

    componhentesequipo_ids = fields.One2many('xestionsat.componhentesequipo', inverse_name='equipo_id')

    ### Campos propios
    nome = fields.Char('Nome', required=True)
    codigo_interno = fields.Char('Código Interno')
    ubicacion = fields.Char('Ubicación')
    descricion = fields.Char('Descrición')
    observacions = fields.Char('Observacións')

    data_alta = fields.Date('Data de Alta', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    data_baixa = fields.Date('Data de Baixa')

    estado = fields.Selection([
        ('almacenado', 'Almacenado'),
        ('operativo', 'Operativo'),
        ('reparandose', 'Reparandose'),
        ('baixa', 'Baixa')],
        'Estado', default="operativo", required=True)

    ### Restriccións
    @api.constrains ('sede_id','usuarios_ids')
    def _comprobar_pai(self):
        for equipo in self:
            if equipo.usuarios_ids and equipo.usuarios_ids.parent_id != equipo.propietario_id:
                raise models.ValidationError('O usuario debe pertencer ó cliente especificado')
            if equipo.sede_id and equipo.sede_id.parent_id != equipo.propietario_id:
                raise models.ValidationError('A sede debe pertencer ó cliente especificado')

    @api.constrains ('codigo_interno')
    def _comprobar_pai(self):
        for equipo in self:
            if  equipo.codigo_interno and self.env['xestionsat.equipos'].search([('codigo_interno', '=', self.codigo_interno), ('id', '!=', self.id)]):
                raise ValueError('O código xa existe')

    @api.constrains ('creado_por_id')
    def _comprobar_creador(self):
        for equipo in self:
            if equipo.creado_por_id and equipo.creado_por_id != self.env.user:
                raise models.ValidationError('Un usuario non pode crear Equipos no nome de outro')

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
