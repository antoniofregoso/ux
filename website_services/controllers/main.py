# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class WebsiteServices(http.Controller):
    
    @http.route(['/services/get_services'], type='json', auth='public', website=True)
    def get_services(self, template):
        services = request.env['product.template'].search([('landig_page_published', '=', True), ('sale_ok', '=', True)], order="sequence" )
        
        return request.website.viewref(template).render({'services': services})