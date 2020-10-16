# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteLegalPage(http.Controller):
#     @http.route('/website_legal_page/website_legal_page/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_legal_page/website_legal_page/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_legal_page.listing', {
#             'root': '/website_legal_page/website_legal_page',
#             'objects': http.request.env['website_legal_page.website_legal_page'].search([]),
#         })

#     @http.route('/website_legal_page/website_legal_page/objects/<model("website_legal_page.website_legal_page"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_legal_page.object', {
#             'object': obj
#         })
