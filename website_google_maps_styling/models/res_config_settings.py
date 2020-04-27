# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    google_map_theme_id  = fields.Many2one('google_map.theme', string ='Maps Theme',  related='website_id.google_map_theme_id', readonly=False)