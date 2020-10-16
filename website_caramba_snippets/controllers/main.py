

from odoo import http, fields
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class WebsiteCaramba(http.Controller):
    
    @http.route(['/caramba/get_social_media'], type='json', auth='public', website=True)
    def get_social_media(self, template):
        site = request.website
        res = []
        if site.social_facebook:
            res.append({'url':site.social_facebook, 'icon': 'fa-facebook-square'})
        if site.social_twitter:
            res.append({'url':site.social_twitter, 'icon': 'fa-twitter'})
        if site.social_linkedin:
            res.append({'url':site.social_linkedin, 'icon': 'fa-linkedin'})
        if site.social_youtube:
            res.append({'url':site.social_youtube, 'icon': 'fa-youtube-play'})
        if site.social_github:
            res.append({'url':site.social_github, 'icon': 'fa-github'})
        if site.social_instagram:
            res.append({'url':site.social_instagram, 'icon': 'fa-instagram'})
        return request.website.viewref(template)._render({'social_media': res})
