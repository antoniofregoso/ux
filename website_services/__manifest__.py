# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
{
    'name': "Website Services",

    'summary': "Add service snippets to the web page",

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.com",

    'category': 'Website/Website',
    'version': '0.0.0',
    'license': 'AGPL-3',

    
    'depends': ['website_sale', 'website_swiper'],

    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        #'views/website_services_templates.xml',
        #'views/website_services_snippets.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
