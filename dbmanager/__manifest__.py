# -*- encoding: utf-8 -*-
##############################################################################
#
# Released under LGPL v.3
#
##############################################################################

{
    "name": "Database Manager",
    "version": "16.0.1.0.0",
    "category": "Configuration",
    "description": "",
    "author": "Luca Vercelli",
    "website": "",
    "depends": [
        "base"
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/create_views.sql',
    ],
    "init_xml": [],
    "update_xml": [],
    "demo_xml": [],
    "test": [],
    "installable": True,
    "active": False,
	"license" : 'LGPL-3',
	"application" : True,
}
