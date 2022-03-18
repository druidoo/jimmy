# -*- coding: utf-8 -*-
{
    'name': "Jimmy Fairly Sale",

    'summary': """
        This module allows us to add customization to sales module""",
    'sequence': -99,
    'author': "Arkeup",
    'website': 'https://arkeup.com',
    'license': 'AGPL-3',
    'category': 'Sales',
    'version': '1.0',

    'depends': ['sale_management', 'jf_base'],

    'data': [
        'views/sale_order_views.xml',
        'views/res_partner_views.xml'
    ],
}
