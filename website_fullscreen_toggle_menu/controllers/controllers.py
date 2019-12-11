# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteFullscreenToggleMenu(http.Controller):
#     @http.route('/website_fullscreen_toggle_menu/website_fullscreen_toggle_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_fullscreen_toggle_menu/website_fullscreen_toggle_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_fullscreen_toggle_menu.listing', {
#             'root': '/website_fullscreen_toggle_menu/website_fullscreen_toggle_menu',
#             'objects': http.request.env['website_fullscreen_toggle_menu.website_fullscreen_toggle_menu'].search([]),
#         })

#     @http.route('/website_fullscreen_toggle_menu/website_fullscreen_toggle_menu/objects/<model("website_fullscreen_toggle_menu.website_fullscreen_toggle_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_fullscreen_toggle_menu.object', {
#             'object': obj
#         })
