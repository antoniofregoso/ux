# -*- coding: utf-8 -*-


from odoo import api, fields, models


class Website(models.Model):
    _inherit = 'website'
    
    alert_color = fields.Char(string="Background Color", help="Choose your color", default="#ff0000")
    
    
    
    