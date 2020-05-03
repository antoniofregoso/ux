# -*- coding: utf-8 -*-

import json

from odoo import http
from odoo.http import request
from odoo.tools import html_escape as escape
import logging

_logger = logging.getLogger(__name__)

class GoogleMap(http.Controller):
    
        
    @http.route(['/map'], type='http', auth="public", website=True, sitemap=False)
    def google_map(self,company, **kw):
        partner = request.env['res.partner'].sudo().search([("id", "=", company),
                                                             ('website_published', '=', True), ('is_company', '=', True)])
        site = request.website
        google_maps_api_key = site.google_maps_api_key
        if len(partner) ==1:
            jsn_theme = site.get_map_styles()
            lat = partner.partner_latitude
            lng = partner.partner_longitude
            values = {'lat':lat, 'lng':lng, 'styles':jsn_theme,'api_key':google_maps_api_key}
        return request.render("website_google_maps_styling.company_google_map", values)
    

         
        

    