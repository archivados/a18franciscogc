###############################################################################
# Constants to manage MESSAGES
###############################################################################
MESSAGE = {
    ###########################################################################
    # INCICENCE
    ###########################################################################
    # -------------------------------------------------------------------------
    # Errors
    # -------------------------------------------------------------------------
    'incidence_error': {
        'close': 'OPERATION NOT AVAILABLE: To close an Incidence you must'
        ' do it using the "Close Incidence" button',

        'invoiced': 'OPERATION NOT AVAILABLE: The status is invoiced'
        ' Incidences cannot be changed',

        'locked': 'OPERATION NOT AVAILABLE: The status is locked'
        ' Incidences cannot be changed',

        'date_end': 'There are {0} unclosed actions. All actions need'
        ' to be closed in order to close the Incidence',

        'operation': 'An error has occurred and the operation could not'
        ' be completed:\n\n',
    },
    # -------------------------------------------------------------------------
    # Constraints
    # -------------------------------------------------------------------------
    'incidence_constraint': {
        'parent': 'The Device must belong to the specified Customer',

        'created_by_id': 'One User cannot create Incidences in the name of'
        'another',

        'date_end': 'The end date cannot be earlier than the start date',

        'invoiced': 'The incidence is already on the invoicing circuit',

        'unlink': 'OPERATION NOT ALLOWED: Cannot delete Incidence is associated'
        ' with another record',
    },
    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------
    'incidence_methods': {
        'add_action': 'Automatic process completed, please check that the'
        ' result is correct',

        '_get_invoice_order': 'Automatic process completed, please check'
        ' that the result is correct.',
    },

    ###########################################################################
    # INCICENCE ACTIONS
    ###########################################################################
    # -------------------------------------------------------------------------
    # Errors
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Constraints
    # -------------------------------------------------------------------------
    'action_constraint': {
        'executed_by': 'One user cannot create Actions in the name of another',

        'date_end': 'The end date cannot be earlier than the start date',
    },
    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------
    'action_methods': {
        'close_action_tilte': 'OPERATION NOT ALLOWED',

        'close_action': 'You cannot reopen actions with the incidence closed.'

        ' If you want to modify the action, please reopen the associated'
        ' incidence',
    },

    ###########################################################################
    # INCICENCE STAGES
    ###########################################################################
    # -------------------------------------------------------------------------
    # Errors
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Constraints
    # -------------------------------------------------------------------------
    'stage_constraint': {
        'sequence': 'There can only be one stage per sequence number',
    },
    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    ###########################################################################
    # DEVICE
    ###########################################################################
    # -------------------------------------------------------------------------
    # Errors
    # -------------------------------------------------------------------------
    'device_error': {
        'executed_by': '',
    },
    # -------------------------------------------------------------------------
    # Constraints
    # -------------------------------------------------------------------------
    'device_constraint': {
        'headquarter_id': 'The Headquarters must belong to the specified'
        ' Customer',

        'user_ids': 'The Device User must be a member  of the specified'
        ' Customer',

        'date_cancellation': 'The cancellation date cannot be earlier than the'
        ' registration date',

        'internal_id': 'The code already exists',

        'created_by_id': 'One User cannot create Devices in the name of'
        ' another',

        'unlink': 'OPERATION NOT ALLOWED: Cannot delete Device is associated'
        ' with another record',
    },
    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------
    'device_methods': {
        'change_state': 'Moving from %s to %s is not allowed',

    },

    ###########################################################################
    # DEVICE COMPONENTS
    ###########################################################################
    # -------------------------------------------------------------------------
    # Errors
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Constraints
    # -------------------------------------------------------------------------
    'component_constraint': {
        'executed_by': 'One user cannot create Actions in the name of another',

        'date_cancellation': 'The cancellation date cannot be earlier than the'
        ' registration date',
    },
    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------
}
