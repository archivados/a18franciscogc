# 1: imports of python lib

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules
from .xestionsat_common import NEW_OTHER_DATA

# 5: local imports

# 6: Import of unknown third party lib


class DeviceOtherData(models.Model):
    """Model that describes other information about the device.
    """
    # Private attributes
    _name = 'xestionsat.device.other_data'
    _rec_name = 'data'
    _description = _('Device - Other Data')
    _inherit = ['mail.thread']

    # Default methods

    # Fields declaration

    # Relational Fields
    device_id = fields.Many2one(
        'xestionsat.device',
        string='ID device',
        ondelete='cascade',
        track_visibility=True,
    )

    # Other Fields
    data = fields.Char(
        string='Data',
        required=True,
        track_visibility=True,
    )
    value = fields.Char(
        string='Value',
        required=True,
        track_visibility=True,
    )

    date_registration = fields.Datetime(
        string='Date of registration',
        default=lambda *a: fields.Datetime.now(),
        required=True,
        track_visibility=True,
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges

    # CRUD methods
    @api.multi
    def add_new_data(
        self, name=NEW_OTHER_DATA, context=None, flags=None
    ):
        """Method to create a new add other data to the device according to
        the past context.

        :param name: View title.
        :param context: Context to present the view data.
        :param flags: Flags to modify the view.
        """
        if type(name) != str:
            name = NEW_OTHER_DATA

        return {
            'name': _(name),
            'type': 'ir.actions.act_window',
            'res_model': 'xestionsat.device.other_data',
            'view_type': 'form',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'flags': flags,
        }

    # Action methods

    # Business methods
