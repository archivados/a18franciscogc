# 1: imports of python lib

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class Message(models.TransientModel):
    """Create a view with a custom message.
    """
    _name = 'xestionsat.message'

    message = fields.Text('Message', required=True)
