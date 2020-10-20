# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import http
from odoo.http import request
from colour import Color
import random
import collections
import logging
_logger = logging.getLogger(__name__)

class WebsiteServices(http.Controller):
    
    @http.route(['/tags-cloud/get_tags/cloud/<int:cloud>'], type='json', auth='public', methods=['POST'], website=True)
    def get_tags(self, template, cloud=0):
        ob_cloud = request.env['tags_cloud.tags_cloud'].sudo().search([('id','=',cloud)])[0]
        if ob_cloud.sort == 'highest':
            tags = request.env['tags_cloud.tag'].sudo().search([('tags_cloud_id','=',cloud)], order= 'percentile desc') 
        elif ob_cloud.sort == 'lowest':
            tags = request.env['tags_cloud.tag'].sudo().search([('tags_cloud_id','=',cloud)], order= 'percentile asc')
        else:
            tmp = request.env['tags_cloud.tag'].sudo().search([('tags_cloud_id','=',cloud)])
            i = list(range(0,len(tmp)))
            random.shuffle(i)
            tags = []
            for index in i:
                tags.append(tmp[index])
        data = []
        for tag in tags:
            data.append(tag.percentile)
        top = max(data)
        low = min(data) 
        m = (ob_cloud.font_h2-ob_cloud.font_h1)/(top-low)
        values = collections.Counter(data)
        style = []
        for k, v in  values.items():
            style.append(k)
        levels = len(values)
        color_x1 = Color(ob_cloud.start)
        color_x2 = Color(ob_cloud.end)
        colors = list(color_x1.range_to(Color(color_x2), levels))
        for tag in tags:            
            font_height = str(int(m*tag.percentile + ob_cloud.font_h1))
            if ob_cloud.color == 'gradient':                
                tag.style = 'color: ' + colors[style.index(tag.percentile)].hex + ';  font-size: ' + font_height + 'px;'
            elif ob_cloud.color == 'random-light':
                tag.style = 'color: rgb({},{},{}); '.format(random.randrange(128,255),random.randrange(128,255),random.randrange(128,255))  + 'font-size: ' + font_height + 'px;'
            else:
                tag.style = 'color: rgb({},{},{}); '.format(random.randrange(0,127),random.randrange(0,127),random.randrange(0,127))  + 'font-size: ' + font_height + 'px;'
        return request.website.viewref(template)._render({'tags':tags})
    
