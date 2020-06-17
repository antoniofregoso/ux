# -*- coding: utf-8 -*-
{
    'name': "Website Tag Cloud",

    'summary': "Generate a tag cloud from a list of words ranked in percentiles",



    'author': "Antonio Fregoso  & Russ Porosky",
    'website': "http://antoniofregoso.com",


    'category': 'website',
    'version': '0.1.0',

  
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
