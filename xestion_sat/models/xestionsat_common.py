###########################################################################
# Constants for CRUD messages
###########################################################################
# Device
# -------------------------------------------------------------------------
NEW_DEVICE = 'New Device'

# Device Component
# -------------------------------------------------------------------------
NEW_COMPONENT = 'Add Component'

# Device Other Data
# -------------------------------------------------------------------------
NEW_OTHER_DATA = 'Add Other Data'

# Incidence
# -------------------------------------------------------------------------
NEW_INCIDENCE = 'New Incidence'

# Incidence Action
# -------------------------------------------------------------------------
NEW_ACTION = 'Add Action'

###########################################################################
# Constants for the control of orders and invoices
###########################################################################
# Models
# -------------------------------------------------------------------------
ORDER_MODEL = 'sale.order'
INVOICE_MODEL = 'account.invoice'

# Messages
# -------------------------------------------------------------------------
CREATE_ORDER = 'Create Order and modify it'
CREATE_INVOICE = 'Create Invoice and modify it'

###########################################################################
# Constants to manage views
###########################################################################
COLORS_KANBAN_BOX = {
    'none': 0,
    'red': 1,
    'orange': 2,
    'yellow': 3,
    'light_blue': 4,
    'dark_purple': 5,
    'salmon_pink': 6,
    'medium_blue': 7,
    'dark_blue': 8,
    'fushia': 9,
    'green': 10,
    'purple': 11,
}

COLORS_KANBAN_STATE = {
    'none': ('None', COLORS_KANBAN_BOX['none']),
    'red': ('Red', COLORS_KANBAN_BOX['red']),
    'yellow': ('Yellow', COLORS_KANBAN_BOX['yellow']),
    'green': ('Green', COLORS_KANBAN_BOX['green']),
    'blue': ('Blue', COLORS_KANBAN_BOX['dark_blue']),
}

DECORATION_INCIDENCE_STAGE = {
    'normal': ('Normal', COLORS_KANBAN_BOX['none']),
    'decoration-bf': ('Bold', COLORS_KANBAN_BOX['dark_blue']),
    'decoration-it': ('Italics', COLORS_KANBAN_BOX['salmon_pink']),
    'decoration-danger': ('Light Red', COLORS_KANBAN_BOX['red']),
    'decoration-info': ('Light Blue', COLORS_KANBAN_BOX['light_blue']),
    'decoration-muted': ('Light Gray', COLORS_KANBAN_BOX['none']),
    'decoration-primary': ('Light Purple', COLORS_KANBAN_BOX['purple']),
    'decoration-success': ('Light Green', COLORS_KANBAN_BOX['green']),
    'decoration-warning': ('Light Brown', COLORS_KANBAN_BOX['dark_purple']),
}

DECORATION_ACTION_OPEN = 'decoration-info'
