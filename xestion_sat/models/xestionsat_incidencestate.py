# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


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
