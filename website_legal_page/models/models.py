# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class website_legal_page(models.Model):
#     _name = 'website_legal_page.website_legal_page'
#     _description = 'website_legal_page.website_legal_page'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
