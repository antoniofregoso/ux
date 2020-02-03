# -*- coding: utf-8 -*-
{
    'name': "Creative Commons License",

    'summary': "Provide Creative Commons Licenses",


    'author': "Antonio Fregoso",
    'website': "https://antoniofregoso.com",

    'category': 'Website/Website',
    'version': '13.0.0.0.0',
    'depends': ['website_blog', 'website_caramba_snippets'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_template.xml',
        'views/website_snippets.xml',
        'views/res_config_setting_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
