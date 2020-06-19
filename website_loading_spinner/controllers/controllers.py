# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteLoadingSpinner(http.Controller):
#     @http.route('/website_loading_spinner/website_loading_spinner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_loading_spinner/website_loading_spinner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_loading_spinner.listing', {
#             'root': '/website_loading_spinner/website_loading_spinner',
#             'objects': http.request.env['website_loading_spinner.website_loading_spinner'].search([]),
#         })

#     @http.route('/website_loading_spinner/website_loading_spinner/objects/<model("website_loading_spinner.website_loading_spinner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_loading_spinner.object', {
#             'object': obj
#         })
