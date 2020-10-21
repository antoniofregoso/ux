# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, _
from odoo.tools.translate import html_translate
from odoo.addons.http_routing.models.ir_http import slug

VALUES = {
    'suscribe':_('Subscribe'),
    'apply':_('Apply'),
    'reserve':_('Reserve'),
    'download':_('Download'),
    'get_offer':_('Get Offer'),
    'quote':_('Quote'),
    'sign_up':_('Sign Up'),
    'more_info':_('More Information')
    }




class ProductService(models.Model):
    _name = "product.service"
    _description = "Service Components"
    _order = "sequence, name"
    
    
    def _default_website(self):
        """ Find the first company's website, if there is one. """
        company_id = self.env.company.id

        if self._context.get('default_company_id'):
            company_id = self._context.get('default_company_id')

        domain = [('company_id', '=', company_id)]
        return self.env['website'].search(domain, limit=1)
    
    name = fields.Char('Name', index=True, required=True)
    website_id = fields.Many2one('website', string="Website", ondelete='restrict', default=_default_website)
    sequence = fields.Integer('Sequence', help="Determine the display order", index=True)
    

    



class ProductTemplate(models.Model):
    _inherit = ["product.template"]
    
    landig_page_published = fields.Boolean('On Landing Page', default=False)
    show_price = fields.Boolean('Show Price', default=True)
    service_ids = fields.Many2many('product.service', relation='product_service_combination', string="Service Components", domain="['|',('website_id', '=?', website_id),('website_id', '=', False)]", ondelete='restrict')
    call_to_action = fields.Selection([
        ('suscribe','Subscribe'), 
        ('apply','Apply'),
        ('reserve','Reserve'),
        ('download','Download'),
        ('get_offer','Get Offer'),
        ('quote','Quote'),
        ('sign_up','Sign Up'),
        ('more_info','More Information')
        ], string='Call to Action', default='more_info',)
    button_url = fields.Char('Button URL')
    show_button = fields.Boolean()

    def get_web_value(self,key):
        return VALUES[key]

    



    

    
    

    