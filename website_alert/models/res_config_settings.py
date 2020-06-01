# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    alert_color = fields.Char('Background Color',related='website_id.alert_color', readonly=False)