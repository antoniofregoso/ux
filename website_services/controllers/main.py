# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class WebsiteServices(http.Controller):
    
    @http.route(['/website/get_services'], type='json', auth='public', website=True)
    def get_services(self, template, domain, order='landing_page_order  desc'):
        services = request.env['product.template'].search([('landig_page_published', '=', True)],  order=order)
        return request.website.viewref(template).render({'services': services})