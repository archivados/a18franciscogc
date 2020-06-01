# 1: imports of python lib

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models, fields, api, _

# 4:  imports from odoo modules
from .xestionsat_common import DECORATION_INCIDENCE_STAGE
from .xestionsat_message import MESSAGE

# 5: local imports

# 6: Import of unknown third party lib


class IncidenceStage(models.Model):
    """Model that describes the stages of an incidence.
    """
    ###########################################################################
    # Private attributes
    ###########################################################################
    _name = 'xestionsat.incidence.stage'
    _description = _('Stage in which an incidence is found')
    _rec_name = 'stage'
    _order = "sequence"

    ###########################################################################
    # Default methods
    ###########################################################################
    @api.model
    def _get_default_sequence(self):
        """ Gives default sequence.
        """
        sequence = self.env['xestionsat.incidence.stage'].search([])

        if sequence:
            new_sequence = sequence[len(sequence) - 1].sequence + 1

        return new_sequence if new_sequence else False

    @api.model
    def _get_highlight_items(self):
        """ Get the values for the highlight.
        """
        items = []

        for key, value in DECORATION_INCIDENCE_STAGE.items():
            items.append(
                (key, _(value[0]))
            )
        return items

    @api.model
    def _get_default_highlight(self):
        """ Gives default highlight.
        """
        return list(DECORATION_INCIDENCE_STAGE.keys())[0]

    ###########################################################################
    # Fields declaration
    ###########################################################################
    # -------------------------------------------------------------------------
    # Other Fields
    # -------------------------------------------------------------------------
    stage = fields.Char(
        string='Stage',
        translate=True,
        required=True,
    )
    sequence = fields.Integer(
        string='Sequence',
        default=_get_default_sequence,
        required=True,
        index=True
    )
    description = fields.Text(
        string='Description',
        translate=True,
    )
    highlight = fields.Selection(
        selection=_get_highlight_items,
        string='Highlight',
        default=_get_default_highlight,
        required=True,
    )
    fold = fields.Boolean(
        string='Folded in Pipeline'
    )
    lock_incidence = fields.Boolean(
        string='Lock the Incidence'
    )
    cancel_incidence = fields.Boolean(
        string='Cancel the Incidence'
    )

    ###########################################################################
    # Constraints and onchanges
    ###########################################################################
    @api.constrains('sequence')
    def _check_unique_sequence(self):
        """Verify that the devices associated with the incidence belong to the
        customer.
        """
        for record in self:
            new_sequence = self.env['xestionsat.incidence.stage'].search(
                [('sequence', '=', record.sequence)])
            if len(new_sequence) > 1:
                raise models.ValidationError(
                    _(MESSAGE['stage_constraint']['sequence']))
