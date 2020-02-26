# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteAnimations(http.Controller):
#     @http.route('/website_animations/website_animations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_animations/website_animations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_animations.listing', {
#             'root': '/website_animations/website_animations',
#             'objects': http.request.env['website_animations.website_animations'].search([]),
#         })

#     @http.route('/website_animations/website_animations/objects/<model("website_animations.website_animations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_animations.object', {
#             'object': obj
#         })
