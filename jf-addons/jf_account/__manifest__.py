# -*- coding: utf-8 -*-
{
    'name': "Jimmy Fairly Account",

    'summary': """
        This module allows us to add customization to account module""",

    'sequence': -99,
    'author': "Arkeup",
    'website': 'https://arkeup.com',
    'license': 'AGPL-3',
    'category': 'Account',
    'version': '1.0',
    'depends': ['account', 'jf_base'],

    # always loaded
    'data': [
        'views/res_partner_views.xml',
    ],
}
