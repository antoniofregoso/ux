# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteLateralMenu(http.Controller):
#     @http.route('/website_lateral_menu/website_lateral_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_lateral_menu/website_lateral_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_lateral_menu.listing', {
#             'root': '/website_lateral_menu/website_lateral_menu',
#             'objects': http.request.env['website_lateral_menu.website_lateral_menu'].search([]),
#         })

#     @http.route('/website_lateral_menu/website_lateral_menu/objects/<model("website_lateral_menu.website_lateral_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_lateral_menu.object', {
#             'object': obj
#         })
