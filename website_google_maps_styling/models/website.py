# -*- coding: utf-8 -*-


from odoo import api, fields, models



class Website(models.Model):
    _inherit = 'website'
    
    google_map_theme_id = fields.Many2one('google_map.theme', string='Maps Theme')