# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteSwiper(http.Controller):
#     @http.route('/website_swiper/website_swiper/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_swiper/website_swiper/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_swiper.listing', {
#             'root': '/website_swiper/website_swiper',
#             'objects': http.request.env['website_swiper.website_swiper'].search([]),
#         })

#     @http.route('/website_swiper/website_swiper/objects/<model("website_swiper.website_swiper"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_swiper.object', {
#             'object': obj
#         })
