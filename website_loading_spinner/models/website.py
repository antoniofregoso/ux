# -*- coding: utf-8 -*-


from odoo import api, fields, models



class Website(models.Model):
    _inherit = 'website'
    
    loader_style = fields.Selection([
        ('loader', 'Bars'), 
        ('loader4', 'Dots'), 
        ('loader5', 'Dotted Circle'), 
        ('loader6', 'Dotted Comet'), 
        ('loader7', '3 Dots'), 
        ('loader8', 'Circular Path'), 
        ], text='Loading Spinner', default='loader')