# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteServices(http.Controller):
#     @http.route('/website_services/website_services/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_services/website_services/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_services.listing', {
#             'root': '/website_services/website_services',
#             'objects': http.request.env['website_services.website_services'].search([]),
#         })

#     @http.route('/website_services/website_services/objects/<model("website_services.website_services"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_services.object', {
#             'object': obj
#         })
