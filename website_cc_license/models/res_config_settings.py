# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cc_license = fields.Boolean('CC License', related='website_id.cc_license', readonly=False)
    cc_share = fields.Selection('Allow adaptations', related='website_id.cc_share', readonly=False)
    cc_commercial = fields.Boolean('Commercial uses', related='website_id.cc_commercial', readonly=False)
    cc_metadata_title = fields.Boolean('Title', related='website_id.cc_metadata_title', readonly=False)
    cc_metadata_attribution = fields.Selection('Attribution', related='website_id.cc_metadata_attribution', readonly=False)
    cc_compact_icon = fields.Boolean('Compact icon', related='website_id.cc_compact_icon', readonly=False)
