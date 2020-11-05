# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request

class WebsiteServices(http.Controller):

    
    @http.route(['/services/get_services'], type='json', auth='public', website=True)
    def get_services(self, template):
        domain = [('landig_page_published', '=', True), ('sale_ok', '=', True), '|', ('website_id','=', request.website.id), ('website_id','=', False)]
        services = request.env['product.template'].sudo().search(domain, order="sequence" )
        values = {'suscribe':_('Subscribe'),'apply':_('Apply'),'reserve':_('Reserve'),'download':_('Download'),'get_offer':_('Get Offer'),'quote':_('Quote'),'sign_up':_('Sign Up'),'more_info':_('More Information')}
        return request.website.viewref(template)._render({'services': services, 'call_to_action':values})


