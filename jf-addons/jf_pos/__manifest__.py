# -*- coding: utf-8 -*-
{
    'name': "Jimmy Fairly POS",

    'summary': """
        This module allows us to add customization to point of sale module""",
    'sequence': -99,
    'author': "Arkeup",
    'website': 'https://arkeup.com',
    'license': 'AGPL-3',
    'category': 'Sales',
    'version': '1.0',
    'depends': ['pos_sale', 'jf_base'],

    # always loaded
    'data': [
        'views/pos_config_views.xml',
        'views/pos_order_views.xml',
        'views/res_partner_views.xml',
        'views/eye_info_views.xml',
    ],
}
