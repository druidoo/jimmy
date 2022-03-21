# -*- coding: utf-8 -*-
{
    'name': "Jimmy Fairly Base",

    'summary': """
        All Jimmy Fairly's module depends on this module""",
    'sequence': -99,
    'author': "Arkeup",
    'website': 'https://arkeup.com',
    'license': 'AGPL-3',
    'category': 'Customizations',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/eye_info_views.xml',
        'views/ir_attachment_views.xml',
        'views/res_partner_views.xml'
    ],
}
