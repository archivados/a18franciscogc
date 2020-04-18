# -*- coding: utf-8 -*-
{
    'name': "xestionSAT",

    'summary': """
        Módulo para manexar a xestión dun Servizo de Asistencia Técnica""",

    'description': """
        Preténdese modelar un módulo que facilite o rexistro das intervencións técnicas sobre un ou varios Equipos relacionados cuns clientes (Partners) e a consulta do histórico das mesmas.

        Funcionalidades
           - Dar de alta unha Incidencia
           - Rexistrar unha Actuación sobre unha Incidencia dada
           - Crear novas Accións para poder asignar a unha Actuación
           - Crear Actuacións sen ser unha Acción rexistrada
           - Dar de alta un Equipo
           - Rexistrar/Editar/Borrar un Compoñente dun Equipo
    """,

    'author': "Fco. Javier Gonzalez Campos",
    'website': "https://github.com/a18franciscogc/xestionSAT",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '12.0.0.5.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base', 'sale_management', 'hr', 'calendar', 'crm'],
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        'data/xestionsat_incidence_assistance_place.xml',
        'data/xestionsat_incidence_state.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/xestionsat_main_menu.xml',
        'views/xestionsat_device.xml',
        'views/xestionsat_device_component.xml',
        'views/xestionsat_incidence.xml',
        'views/xestionsat_incidence_assistance_place.xml',
        'views/xestionsat_incidence_state.xml',
        'views/xestionsat_incidence_action.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #    'demo/demo.xml',
    # ],
}