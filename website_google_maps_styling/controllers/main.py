# -*- coding: utf-8 -*-

import json

from odoo import http
from odoo.http import request
from odoo.tools import html_escape as escape

import logging

_logger = logging.getLogger(__name__)

class GoogleMap(http.Controller):
    
    @http.route(['/google_map_theme'], type='json', auth="public", website=True, sitemap=False)
    def google_map_theme(self, template):
        theme = request.website.google_map_theme_id
        js_theme = []
        if theme:   
            if theme.geometry_visibility:
                js_theme.append({"elementType": "geometry","stylers":[{ "color":theme.geometry_color}]})
            else:
                js_theme.append({"elementType": "geometry","stylers":[{ "visibility":"off"}]})
            if not theme.labels_icon:
                js_theme.append({"elementType": "labels.icon","stylers":[{ "visibility":"off"}]})
            if theme.text_stroke_visibility:
                js_theme.append({"elementType": "labels.text.stroke","stylers":[{ "color":theme.text_stroke_color}]}) 
            else:
                js_theme.append({"elementType": "labels.text.stroke","stylers":[{ "visibility":"off"}]})  
            if theme.text_fill_visibility:
                js_theme.append({"elementType": "labels.text.fill","stylers":[{ "color":theme.text_fill_color}]})
            else:
                js_theme.append({"elementType": "labels.text.fill","stylers":[{ "visibility":"off"}]})  
            for option in theme.options_ids:
                js_option = {"featureType": option.feature, "elementType": option.element , "stylers":[]}
                if option.visibility:
                    js_option["stylers"]= [{"color":option.color}]
                else:
                    js_option["stylers"]= [{"visibility": "off"}] 
                js_theme.append(js_option)         
            return request.website.viewref(template).render({'theme': js_theme})
        
    @http.route(['/map'], type='http', auth="public", website=True, sitemap=False)
    def google_map(self,company, **kw):
        partner = request.env['res.partner'].sudo().search([("id", "=", company),
                                                             ('website_published', '=', True), ('is_company', '=', True)])
        if len(partner) ==1:
            theme = request.website.google_map_theme_id
            js_theme = []
            if theme:   
                if theme.geometry_visibility:
                    js_theme.append({"elementType": "geometry","stylers":[{ "color":theme.geometry_color}]})
                else:
                    js_theme.append({"elementType": "geometry","stylers":[{ "visibility":"off"}]})
                if not theme.labels_icon:
                    js_theme.append({"elementType": "labels.icon","stylers":[{ "visibility":"off"}]})
                if theme.text_stroke_visibility:
                    js_theme.append({"elementType": "labels.text.stroke","stylers":[{ "color":theme.text_stroke_color}]}) 
                else:
                    js_theme.append({"elementType": "labels.text.stroke","stylers":[{ "visibility":"off"}]})  
                if theme.text_fill_visibility:
                    js_theme.append({"elementType": "labels.text.fill","stylers":[{ "color":theme.text_fill_color}]})
                else:
                    js_theme.append({"elementType": "labels.text.fill","stylers":[{ "visibility":"off"}]})  
                for option in theme.options_ids:
                    js_option = {"featureType": option.feature, "elementType": option.element , "stylers":[]}
                    if option.visibility:
                        js_option["stylers"]= [{"color":option.color}]
                    else:
                        js_option["stylers"]= [{"visibility": "off"}] 
                    js_theme.append(js_option)
            lat = partner.partner_latitude
            lng = partner.partner_longitude
            values = {'lat':lat, 'lng':lng, 'styles':js_theme}
        return request.render("website_google_maps_styling.company_google_map", values)
         
         
        

    