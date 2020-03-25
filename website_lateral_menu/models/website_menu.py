
from odoo import api, fields, models

class Menu(models.Model):
    _inherit = 'website.menu'
    
    icon = fields.Char('Icon', default="fa fa-2x fa-home")