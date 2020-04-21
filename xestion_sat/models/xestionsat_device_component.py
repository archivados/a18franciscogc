# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class DeviceComponent(models.Model):
    """Model to describe the components that make up each device.
    """

    # Private attributes
    _name = 'xestionsat.device.component'
    _inherits = {'product.template': 'template_id'}

    # Default methods

    # Fields declaration
    # Relational Fields
    template_id = fields.Many2one(
        'product.template',
        string='Compponent',
        ondelete='cascade',
        required=True,
    )
    device_id = fields.Many2one(
        'xestionsat.device',
        string='ID device',
        ondelete='cascade',
        required=True,
    )

    # Other Fields
    # nome = fields.Char('Nome descriptivo', required=True)
    serial = fields.Char(
        string='Serial number',
    )
    observation = fields.Char(
        string='Observations',
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges
