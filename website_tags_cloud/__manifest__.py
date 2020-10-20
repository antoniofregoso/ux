# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Website Tag Cloud",

    'summary': "Generate a tag cloud from a list of words ranked in percentiles",



    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.com",


    'category': 'website',
    'version': '0.0.0',
    'license': 'AGPL-3',

  
    'depends': ['website'],


    'data': [
        'security/ir.model.access.csv',
        'views/website_tags_cloud_views.xml',
        'views/website_tags_cloud_snippets.xml',
        'views/website_tags_cloud_templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
