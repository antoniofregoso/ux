# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class WebsiteServices(http.Controller):
    
    @http.route(['/services/get_services'], type='json', auth='public', methods=['POST'], website=True)
    def get_services(self, template):
        services = request.env['product.template'].search([('landig_page_published', '=', True), ('sale_ok', '=', True), '|', ('website_id','=', request.website.id), ('website_id','=', False)], order="sequence" )
        _logger.warn('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc: {}:'.format(len(services)))
        return request.website.viewref(template).render({'services': services})