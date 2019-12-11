# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class website_event_floating_menu(models.Model):
#     _name = 'website_event_floating_menu.website_event_floating_menu'
#     _description = 'website_event_floating_menu.website_event_floating_menu'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
