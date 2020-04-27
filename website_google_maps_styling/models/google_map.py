# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

    
class GoogleMapOption(models.Model):
    _name = "google_map.option"
    _description = "Google Map Option"
    
    feature = fields.Selection([
        ('administrative', 'Administrative'),
        ('administrative.country', 'Administrative Country'),
        ('administrative.province', 'Administrative Province'),
        ('administrative.locality', 'Administrative Locality'),
        ('administrative.land_parcel', 'Administrative Land Parcel'),
        ('landscape.man_made', 'Landscape Man Made'),
        ('landscape.natural', 'Landscape Natural'),
        ('poi', 'Point of Interest'),
        ('poi.park', 'POI Park'),
        ('road', 'Road'),
        ('road.local', 'Road Local'),
        ('road.arterial', 'Road Arterial'),
        ('road.highway', 'Road Highway'),
        ('road.highway.controlled_access', 'Road Highway Controlled Access'),
        ('transit', 'Transit'),
        ('transit.line', 'Transit Line'),
        ('transit.station', 'Transit Station'),
        ('water', 'Water')
        ], required=True)
    element = fields.Selection([
        ('geometry', 'Geometry'),
        ('geometry.stroke', 'Geometry Stroke'),
        ('geometry.fill', 'Geometry Fill'),
        ('labels.text.stroke', 'Text Stroke'),
        ('labels.text.fill', 'Text Fill')])
    color = fields.Char('Color')
    visibility = fields.Boolean('Visibility', default=True , required=True)
    map_id = fields.Many2one('google_map.theme')
    

class GooleMapTheme(models.Model):
    _name = "google_map.theme"
    _description = "Google Maps Themes"
    
    name = name = fields.Char('Name', index=True, required=True)
    roads_density = fields.Selection([('none', 'Nome'), ('low', 'Low'), ('medium', 'Medium'), ('height', 'Height')], string="Roads", defautl=3)
    landmarks_density = fields.Selection([('none', 'Nome'), ('low', 'Low'), ('medium', 'Medium'), ('height', 'Height')], string="Landmarks", defautl=3)
    labels_density = fields.Selection([('none', 'Nome'), ('low', 'Low'), ('medium', 'Medium'), ('height', 'Height')], string="Labels", defautl=3)
    geometry_color = fields.Char('Geometry Color')
    geometry_visibility = fields.Boolean('Geometry Visibility', default=True)
    labels_icon = fields.Boolean('Labels Icon Visibility', default=True) 
    text_stroke_color = fields.Char('Stroke Color')
    text_stroke_visibility = fields.Boolean('Stroke Visibility', default=True)
    text_fill_color = fields.Char('Text Fill Color')
    text_fill_visibility = fields.Boolean('Text Fill Visibility', default=True)
    options_ids = fields.One2many('google_map.option', 'map_id', string='Options', ondelete='cascade')
    image = fields.Image("Image", max_width=300, max_height=200)
    