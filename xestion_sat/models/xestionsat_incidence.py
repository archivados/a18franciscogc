# 1: imports of python lib
from datetime import datetime

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class Incidence(models.Model):
    """Model to manage the information of an incidence.
    """

    # Private attributes
    _name = 'xestionsat.incidence'
    _description = _('Incidence associated with a Customer')
    _rec_name = 'title'
    _order = 'date_start desc'

    # Default methods

    # Fields declaration
    # Relational Fields
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        ondelete='restrict',
        required=True,
    )
    device_ids = fields.Many2many(
        'xestionsat.device',
        string='Devices',
        required=True,
    )
    created_by_id = fields.Many2one(
        'res.users',
        string='Created by',
        ondelete='restrict',
        default=lambda self: self.env.user,
        required=True,
    )

    incidence_action_ids = fields.One2many(
        'xestionsat.incidence.action',
        string='Incidence Actions',
        inverse_name='incidence_id',
    )

    date_start = fields.Date(
        string='Date start',
        default=lambda *a: datetime.now().strftime('%Y-%m-%d')
    )
    date_end = fields.Date(
        string='Date ends',
    )

    state = fields.Many2one(
        'xestionsat.incidence.state',
        string='State',
    )

    assistance_place = fields.Many2one(
        'xestionsat.incidence.assistance_place',
        string='Place of assistance',
    )

    # Other Fields
    title = fields.Char(
        string='Title',
        required=True,
    )
    failure_description = fields.Char(
        string='Description of the failure',
        required=True,
    )
    observation = fields.Char(
        string='Observations',
    )
    lock = fields.Boolean(
        string='Lock',
        default=False,
        readonly=True,
    )

    # compute and search fields, in the same order that fields declaration

    # Constraints and onchanges
    @api.constrains('device_ids')
    def _check_father(self):
        """Verify that the devices associated with the incidence belong to the
        customer.
        """

        error_message = 'The Device must belong to the specified Customer'

        for incidencia in self:
            for device in incidencia.device_ids:
                if device and device.owner_id != incidencia.customer_id:
                    raise models.ValidationError(_(error_message))

    @api.constrains('created_by_id')
    def _check_created_by_id(self):
        """Verify that incidence creation is not assigned to a different
        system user than the one running the application.
        """

        error_message = 'One User cannot create Incidences in the name of' \
            'another'

        for incidencia in self:
            if incidencia.created_by_id \
                    and incidencia.created_by_id != self.env.user:
                raise models.ValidationError(_(error_message))
