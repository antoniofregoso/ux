# -*- coding: utf-8 -*-


from odoo import api, fields, models


class Website(models.Model):
    _inherit = 'website'
    
    alert_color = fields.Char(string="Background Color", help="Choose your color", default="#ff0000")
    alert_message_color = fields.Char(string="Message Color", help="Choose your color", default="#ffffff")
    alert_title =  fields.Char('Title', default="Important Message")
    alert_message1 = fields.Char('Message 1', default="Aww yeah, you successfully read this important alert message")
    alert_message2 = fields.Char('message 2', default="Aww yeah, you successfully read this important alert message")
    alert_covid_enabled = fields.Boolean(default=True)
    
    
    
    