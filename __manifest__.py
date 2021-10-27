# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'insurance_pharmacie',
    'version': '1.0',
    'category': 'point_of_sale',
    'sequence': 10,
    'summary': 'Application de gestion de pharmacie',
    'description': """Application de gestion de pharmacie""",
    'depends': ['point_of_sale','base'],
    'data':[
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/souscripteur_views.xml',
        'views/assureur_views.xml',
        'views/account_views.xml',
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'qweb': [

    ],
    'website': '',
    'license': 'LGPL-3',
}

