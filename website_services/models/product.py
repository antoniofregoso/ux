# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = ["product.template"]
    
    landig_page_published = fields.Boolean(default=False)
    landing_page_order = fields.Integer('Landing Page Order')
    