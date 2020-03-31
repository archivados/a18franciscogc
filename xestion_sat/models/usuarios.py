# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api

class Usuarios(models.Model):
    ### Campos modelo
    _name = 'xestionsat.usarios'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'XestionSAT Usuarios'