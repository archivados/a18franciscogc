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

    ### Cambios de Estado
    @api.model
    def cambios_estado_permitidos(self, estado_actual, estado_novo):
        allowed = [('almacenado', 'operativo'),
                   ('almacenado', 'reparandose'),
                   ('almacenado', 'baixa'),

                   ('operativo', 'almacenado'),
                   ('operativo', 'reparandose'),
                   ('operativo', 'baixa'),
                   
                   ('reparandose', 'almacenado'),
                   ('reparandose', 'operativo'),
                   ('reparandose', 'baixa'),

                   ('baixa', 'almacenado'),
                   ('baixa', 'operativo'),
                   ('baixa', 'reparandose')]
        return (estado_actual, estado_novo) in allowed

    @api.multi
    def cambiar_estado(self, estado_novo):
        for equipo in self:
            if equipo.estado != estado_novo:
                if equipo.cambios_estado_permitidos(equipo.estado, estado_novo):
                    equipo.estado = estado_novo
                else:
                    mensaxe = ('Non se pode cambiar de <%s> a <%s>') % (equipo.estado, estado_novo)
                    raise models.UserError(mensaxe)

    def almacenar(self):
        self.cambiar_estado('almacenado')

    def ponher_operativo(self):
        self.cambiar_estado('operativo')

    @api.multi
    def crear_incidencia(self):
        self.cambiar_estado('reparandose')        

        return self.crear_incidencia_nova()

    '''
    @api.multi
    def comprobar_incidencias(self):
        ten_incidencias = False

        for inicidencia in self.env['xestionsat.incidencias'].search([]):
            domain = ['&',('equipos.id', 'in', inicidencia.equipos_ids), ('estado', '=', 'reparandose')]
            ten_incidencias = self.env['xestionsat.incidencias'].search(domain, count=True) > 0
        
        return ten_incidencias
    '''
     
    @api.multi
    def crear_incidencia_nova(self):
        incidencia_form = self.env.ref('xestionsat.incidencias', False)

        incidencia_nova_contexto = {
            'default_bloquear': True,
            'default_cliente_id': self.propietario_id.id,
            'default_equipos_ids': [ self.id ]
        }

        incidencia_nova = {
            'name': 'Nova Incidencia',
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.incidencias',
            'view_type': 'form',
            'view_mode': 'form',
            'context': incidencia_nova_contexto,
            'target': 'new',
            'views': [(incidencia_form, 'form')],
            'view_id': incidencia_form,
            'flags': {'action_buttons': True}
        }

        #record = self.env['xestionsat.incidencias'].create(incidencia_nova)
        return incidencia_nova

    def dar_baixa(self):
        self.cambiar_estado('baixa')

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
