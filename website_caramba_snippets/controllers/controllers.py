# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteCarambaSnippets(http.Controller):
#     @http.route('/website_caramba_snippets/website_caramba_snippets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_caramba_snippets/website_caramba_snippets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_caramba_snippets.listing', {
#             'root': '/website_caramba_snippets/website_caramba_snippets',
#             'objects': http.request.env['website_caramba_snippets.website_caramba_snippets'].search([]),
#         })

#     @http.route('/website_caramba_snippets/website_caramba_snippets/objects/<model("website_caramba_snippets.website_caramba_snippets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_caramba_snippets.object', {
#             'object': obj
#         })
