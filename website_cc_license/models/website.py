# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = 'website'
    
    cc_license = fields.Boolean('CC License', help='Active creative commons license', default=False)
    cc_share = fields.Selection([ ('by','Yes'), ('by-nd','No'), ('by-sa', 'Yes, as long as others share alike ')],'Allow adaptations', help='Allow adaptations of your work to be shared?', default='by-nd')
    cc_commercial = fields.Boolean('Commercial uses', help='Allow commercial uses of your work?', default=False)
    cc_metadata_title = fields.Boolean('Title', help='Do you want to include title of work?',  default=False)
    cc_metadata_attribution = fields.Selection([ ('no','No'), ('author','Author'),('company','Company')],'Attribution', help='Do you want to include attribution for the author?', default='no')
    cc_compact_icon = fields.Boolean('Compact icon', help="Normal icon: 88x31 px, compact icon: 80x15 px", default=False)
    
     
    def get_blogs(self):
        res = self.env['blog.blog'].sudo().search(['|',('website_id','=', self.id),('website_id', '=', False)])
        return res
        
             
    def get_cc(self):
        lc_text = ""
        lc_url = "http://creativecommons.org/licenses/"
        lc_img = "https://i.creativecommons.org/l/"
        if self.cc_commercial:
            if self.cc_share=='by':
                lc_text += _("Creative Commons Attribution 4.0 International License")
                lc_url += "by/4.0/" 
                lc_img += "by/4.0/"              
            elif self.cc_share=='by-nd':
                lc_text += _("Creative Commons Attribution-WithoutDerive 4.0 International License")
                lc_url += "by-nd/4.0/"
                lc_img += "by-nd/4.0/"        
            else:
                lc_text += _("Creative Commons Attribution-ShareAlike 4.0 International License")
                lc_url += "by-sa/4.0/"
                lc_img += "by-sa/4.0/"                             
        else:
            if self.cc_share=='by':
                lc_text += _("Creative Commons Attribution- NonCommercial 4.0 International License")
                lc_url += "by-nc/4.0/" 
                lc_img += "by-nc/4.0/"                
            elif self.cc_share=='by-nd':
                lc_text += _("Creative Commons Attribution-NonCommercial-WithoutDerive 4.0 International License")
                lc_url += "by-nc-nd/4.0/"
                lc_img += "by-nc-nd/4.0/"       
            else:
                lc_text += _("Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License")
                lc_url += "by-nc-sa/4.0/" 
                lc_img += "by-nc-sa/4.0/"   
        if self.cc_compact_icon: 
            lc_img += "80x15.png"
        else:
            lc_img += "88x31.png"     
        ccl = {'lc_text':lc_text,'lc_url':lc_url, 'lc_img':lc_img, 'lc_metadata_title':self.cc_metadata_title, 'lc_metadata_attribution':self.cc_metadata_attribution} 
        return  ccl