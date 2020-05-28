# -*- coding: utf-8 -*-
{
    'name': "xestionSAT",

    'summary': """
        Module to handle the management of a Technical Assistance Service""",

    'description': """
        It is intended to formalize a module that facilitates the registration
        of interventions techniques on one or more Equipment related to
        customers (Partners) and the consultation of the history of the same.

         Functionalities
            - Register an Incidence
            - Record an Action on a given Incidence
            - Create new Actions to be able to assign to a Performance
            - Create Actions without being a registered Action
            - Register a Team
            - Register / Edit / Delete a Team Component
    """,

    'author': "Fco. Javier Gonzalez Campos",
    'website': "https://github.com/efja/xestionSAT",
    'installable': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/
    #   data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    "license": "AGPL-3",
    'version': '12.0.0.9.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'sale_management'
    ],

    # always loaded
    'data': [
        'data/xestionsat_incidence_assistance_place.xml',
        'data/xestionsat_incidence_stage.xml',

        'security/xestion_sat.xml',
        'security/ir.model.access.csv',

        'views/assets.xml',

        'views/product_template.xml',
        'views/res_partner.xml',

        'wizards/xestionsat_message_view.xml',

        'views/xestionsat_device.xml',
        'views/xestionsat_device_component.xml',
        'views/xestionsat_device_other_data.xml',

        'views/xestionsat_incidence_assistance_place.xml',
        'views/xestionsat_incidence_stage.xml',
        'views/xestionsat_incidence_action.xml',
        'views/xestionsat_incidence.xml',

        'views/xestionsat_main_menu.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #    'demo/demo.xml',
    # ],
}
