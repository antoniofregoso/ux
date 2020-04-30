# -*- coding: utf-8 -*-


from odoo import api, fields, models



class Website(models.Model):
    _inherit = 'website'
    
    google_map_theme_id = fields.Many2one('google_map.theme', string='Maps Theme')
    
    
    def get_map_styles(self):  
        theme = self.google_map_theme_id        
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
                js_option = {"featureType": option.feature}
                if option.element:
                    js_option['elementType'] = option.element
                if option.visibility:
                    js_option["stylers"]= [{"color":option.color}]
                else:
                    js_option["stylers"]= [{"visibility": "off"}] 
                js_theme.append(js_option)
        return js_theme
            