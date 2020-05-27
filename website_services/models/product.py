# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools.translate import html_translate
from odoo.addons.http_routing.models.ir_http import slug



class ProductService(models.Model):
    _name = "product.service"
    _description = "Service Components"
    
    name = fields.Char('Name', index=True, required=True)
    sequence = fields.Integer('Sequence', help="Determine the display order", index=True)
    



class ProductTemplate(models.Model):
    _inherit = ["product.template"]
    
    landig_page_published = fields.Boolean('On Landing Page', default=False)
    service_ids = fields.Many2many('product.service', relation='product_service_combination', string="Service Components", ondelete='restrict')



    

    
    

    