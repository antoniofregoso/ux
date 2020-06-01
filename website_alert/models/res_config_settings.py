# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    alert_color = fields.Char('Background Color',related='website_id.alert_color', readonly=False)
    alert_message_color = fields.Char(string="Message Color", related='website_id.alert_message_color', readonly=False)
    alert_title =  fields.Char('Title',related='website_id.alert_title', readonly=False)
    alert_message1 = fields.Char('Message 1',related='website_id.alert_message1', readonly=False)
    alert_message2 = fields.Char('message 2',related='website_id.alert_message2', readonly=False)