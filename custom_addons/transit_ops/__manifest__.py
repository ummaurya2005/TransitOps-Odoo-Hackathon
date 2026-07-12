{
    'name': 'TransitOps',
    'version': '17.0.1.0.0',
    'summary': 'Smart Transport Operations Platform',
    'description': """
TransitOps
==========
Fleet Management System
Vehicle Management
Driver Management
Trip Management
Maintenance
Fuel & Expense Tracking
Reports & Dashboard
    """,
    'author': 'Team TransitOps',
    'website': 'https://github.com/ummaurya2005/TransitOps-Odoo-Hackathon',

    'category': 'Operations',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'mail',
    ],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/menu.xml',
    ],

    'installable': True,
    'application': True,
}