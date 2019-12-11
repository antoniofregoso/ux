# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    button_side = fields.Selection('Button_side',related='website_id.button_side', readonly=False)
    buttons_color = fields.Selection('Buttons Color', related='website_id.buttons_color', readonly=False)
    whatsapp_enable = fields.Boolean('Enable Whatsapp',related='website_id.whatsapp_enable', readonly=False)
    whatsapp_number = fields.Char('Number', related='website_id.whatsapp_number', readonly=False)
    whatsapp_text = fields.Char('Text', related='website_id.whatsapp_text', readonly=False)
    telegram_enable = fields.Boolean('Enable Telegram', related='website_id.telegram_enable', readonly=False)
    telegram_user = fields.Char('User',related='website_id.telegram_user', readonly=False)
    mesenger_enable = fields.Boolean('Enable Messenger',related='website_id.mesenger_enable', readonly=False)
    messenger_user = fields.Char('User', related='website_id.messenger_user', readonly=False)
    phone_enable = fields.Boolean('Enable Phone', related='website_id.phone_enable', readonly=False)
    phone = fields.Char('Phone', related='website_id.phone', readonly=False)
    
    
    @api.depends('website_id', 'button_side', 'social_facebook', 'social_github', 'social_linkedin', 'social_youtube', 'social_instagram')
    def has_messaging(self):
        self.has_messaging = self.button_side or self.button_color or self.whatsapp_enable \
            or self.whatsapp_number or self.whatsapp_text or self.telegram_enable \
            or self.telegram_user or self.mesenger_enable or self.messenger_user \
            or self.telegram_user or self.mesenger_enable
    def inverse_has_messaging(self):
        if not self.has_messaging:
            self.button_side= 'left'
            self.button_color = 'brand'
            self.whatsapp_enable = ''
            self.whatsapp_number = ''
            self.whatsapp_text = ''
            self.telegram_enable = ''
            self.telegram_user = ''
            self.mesenger_enable = ''
            self.messenger_user = ''

    has_messaging = fields.Boolean("Configure Instant Messaging", compute=has_messaging, inverse=inverse_has_messaging)

