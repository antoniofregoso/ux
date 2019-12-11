# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteEventFloatingMenu(http.Controller):
#     @http.route('/website_event_floating_menu/website_event_floating_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_event_floating_menu/website_event_floating_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_event_floating_menu.listing', {
#             'root': '/website_event_floating_menu/website_event_floating_menu',
#             'objects': http.request.env['website_event_floating_menu.website_event_floating_menu'].search([]),
#         })

#     @http.route('/website_event_floating_menu/website_event_floating_menu/objects/<model("website_event_floating_menu.website_event_floating_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_event_floating_menu.object', {
#             'object': obj
#         })
