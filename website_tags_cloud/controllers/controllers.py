# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteTagCloud(http.Controller):
#     @http.route('/website_tag_cloud/website_tag_cloud/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_tag_cloud/website_tag_cloud/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_tag_cloud.listing', {
#             'root': '/website_tag_cloud/website_tag_cloud',
#             'objects': http.request.env['website_tag_cloud.website_tag_cloud'].search([]),
#         })

#     @http.route('/website_tag_cloud/website_tag_cloud/objects/<model("website_tag_cloud.website_tag_cloud"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_tag_cloud.object', {
#             'object': obj
#         })
