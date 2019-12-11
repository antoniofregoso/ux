# -*- coding: utf-8 -*-
{
    'name': "Website Instant Messaging",

    'summary': 'Integration of floating buttons for instant messaging',

    'description': "",

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Website/Website',
    'version': '13.0.0.1',
    'depends': ['website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_config_setting_view.xml',
        'views/website_instant_messaging_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}