# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteInstantMessaging(http.Controller):
#     @http.route('/website_instant_messaging/website_instant_messaging/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_instant_messaging/website_instant_messaging/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_instant_messaging.listing', {
#             'root': '/website_instant_messaging/website_instant_messaging',
#             'objects': http.request.env['website_instant_messaging.website_instant_messaging'].search([]),
#         })

#     @http.route('/website_instant_messaging/website_instant_messaging/objects/<model("website_instant_messaging.website_instant_messaging"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_instant_messaging.object', {
#             'object': obj
#         })