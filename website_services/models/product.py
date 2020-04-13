# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductService(models.Model):
    _name = "product.service"
    _description = "Product Service"
    
    name = fields.Char('Name', index=True, required=True)
    sequence = fields.Integer('Sequence', help="Determine the display order", index=True)
    


class ProductTemplate(models.Model):
    _inherit = ["product.template"]
    
    landig_page_published = fields.Boolean(default=False)
    service_ids = fields.Many2many('product.service', relation='product_service_combination', string="Services", ondelete='restrict')
    