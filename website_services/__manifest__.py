# -*- coding: utf-8 -*-
{
    'name': "Website Services",

    'summary': "Add service snippets to the web page",

    'author': "Antonio Fregoso",
    'website': "http://antoniofregoso.com",

    'category': 'Website/Website',
    'version': '13.0.0.0.0',

    
    'depends': ['website_caramba_snippets', 'website_sale', 'website_swiper'],

    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/website_services_templates.xml',
        'views/website_services_snippets.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
