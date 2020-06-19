# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    loader_style = fields.Selection('Loading Spinner',related='website_id.loader_style', readonly=False)