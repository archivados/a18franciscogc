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
# Constants to manage models
###########################################################################
# The first item defined is the default
# The second item defined is the default for the incidence model
STATE_DEVICE = [
    ('operational', 'Operational'),
    ('repairing', 'Repairing'),
    ('stored', 'Stored'),
    ('unsubscribe', 'Unsubscribe'),
]

RELOAD_VIEW = {
    'type': 'ir.actions.client',
    'tag': 'reload',
}

# The first item defined is the default
COLOR_KANBAN_BOX = {
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

# The first item defined is the default
COLOR_KANBAN_STATE = {
    'none': ('None', 'none', COLOR_KANBAN_BOX['none']),
    'red': ('Late', 'danger', COLOR_KANBAN_BOX['red']),
    'yellow': ('In progress', 'warning', COLOR_KANBAN_BOX['yellow']),
    'green': ('Done', 'success', COLOR_KANBAN_BOX['green']),
    'blue': ('On hold', 'blue', COLOR_KANBAN_BOX['dark_blue']),
}

# The first item defined is the default
DECORATION_INCIDENCE_STAGE = {
    'normal': ('Normal', COLOR_KANBAN_BOX['none']),
    'decoration-bf': ('Bold', COLOR_KANBAN_BOX['dark_blue']),
    'decoration-it': ('Italics', COLOR_KANBAN_BOX['salmon_pink']),
    'decoration-danger': ('Light Red', COLOR_KANBAN_BOX['red']),
    'decoration-info': ('Light Blue', COLOR_KANBAN_BOX['light_blue']),
    'decoration-muted': ('Light Gray', COLOR_KANBAN_BOX['none']),
    'decoration-primary': ('Light Purple', COLOR_KANBAN_BOX['purple']),
    'decoration-success': ('Light Green', COLOR_KANBAN_BOX['green']),
    'decoration-warning': ('Light Brown', COLOR_KANBAN_BOX['dark_purple']),
}

DECORATION_ACTION_OPEN = 'decoration-info'
