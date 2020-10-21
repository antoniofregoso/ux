# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request





class WebsiteServices(http.Controller):
    
    @http.route(['/services/get_services'], type='json', auth='public', methods=['POST'], website=True)
    def get_services(self, template):
        domain = [('landig_page_published', '=', True), ('sale_ok', '=', True), '|', ('website_id','=', request.website.id), ('website_id','=', False)]
        services = request.env['product.template'].search(domain, order="sequence" )
        return request.website.viewref(template)._render({'services': services})