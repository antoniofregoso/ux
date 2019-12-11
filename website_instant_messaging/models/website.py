# -*- coding: utf-8 -*-


from odoo import api, fields, models



class Website(models.Model):
    _inherit = 'website'
    
    button_side = fields.Selection([('left-messaging-bottom', 'Left'), ('right-messaging-bottom', 'Right')], text='Button_side', default='left-messaging-bottom')
    buttons_color = fields.Selection([('brand','Brand'), ('bg-primary','Primary'), ('bg-secondary','Secondary'), ('bg-success','Success'), ('bg-info','Info')], text='Buttons Color', default='brand')
    whatsapp_enable = fields.Boolean('Enable Whatsapp', default=False)
    whatsapp_number = fields.Char('Whatsapp Number')
    whatsapp_text = fields.Char('Text')
    telegram_enable = fields.Boolean('Enable Telegram', default=False)
    telegram_user = fields.Char('Telegram User')
    mesenger_enable = fields.Boolean('Enable Messenger', default=False)
    messenger_user = fields.Char('Messenger User')
    phone_enable = fields.Boolean('Enable Phone', default=False)
    phone = fields.Char('Phone')
    
    def whatsapp_color(self):
        if self.buttons_color == 'brand':
            return 'st-whatsapp'
        else:
            return self.buttons_color
    
    
    def telegram_color(self):
        if self.buttons_color == 'brand':
            return 'st-telegram'
        else:
            return self.buttons_color
        
    def mesenger_color(self):
        if self.buttons_color == 'brand':
            return 'st-facebook'
        else:
            return self.buttons_color
        
    def phone_color(self):
        if self.buttons_color == 'brand':
            return 'st-phone'
        else:
            return self.buttons_color