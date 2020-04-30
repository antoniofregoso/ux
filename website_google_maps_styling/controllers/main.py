# -*- coding: utf-8 -*-

import json

from odoo import http
from odoo.http import request
from odoo.tools import html_escape as escape


class GoogleMap(http.Controller):
    
        
    @http.route(['/map'], type='http', auth="public", website=True, sitemap=False)
    def google_map(self,company, **kw):
        partner = request.env['res.partner'].sudo().search([("id", "=", company),
                                                             ('website_published', '=', True), ('is_company', '=', True)])
        if len(partner) ==1:
            jsn_theme = request.website.get_map_styles()
            lat = partner.partner_latitude
            lng = partner.partner_longitude
            values = {'lat':lat, 'lng':lng, 'styles':jsn_theme,}
        return request.render("website_google_maps_styling.company_google_map", values)
    

         
        

    