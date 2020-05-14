# 1: imports of python lib
from datetime import datetime

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
    _description = _('Component that is part of a Device')
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
    )

    # Other Fields
    serial = fields.Char(
        string='Serial number',
    )
    observation = fields.Char(
        string='Observations',
    )

    date_registration = fields.Date(
        string='Date of registration',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d'),
        required=True,
    )
    date_cancellation = fields.Date(
        string='Date of cancellation'
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges

    # CRUD methods
    @api.multi
    def create_new_component(
        self, name='Add component', context=None, flags=None
    ):
        """Method to create a new add component according to the past context.
        """

        return {
            'name': _(name),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.device.component',
            'view_type': 'form',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'flags': flags,
        }

    # Action methods

    # Business methods
