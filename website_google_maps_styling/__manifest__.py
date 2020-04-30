# -*- coding: utf-8 -*-
{
    'name': "Website Google Maps Styling",

    'summary': "Allows you to add custom styles to Google Maps",


    'author': "Antonio Fregoso",
    'website': "https://antoniofregoso.com",
    'category': 'Website/Website',
    'version': '13.0.0.0.0',

    'depends': ['website_google_map','website_form'],

    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_view.xml',
        'views/website_google_maps_views.xml',
        'views/website_google_maps_templates.xml',
        'data/website_google_maps_styling_data.xml'
    ],

}
