# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
import logging
_logger = logging.getLogger(__name__)


class BlogTag(models.Model):    
    _inherit = 'blog.tag'
    
    
    def get_tag_cloud(self):
        if self.post_ids:
            query = """select t.id,  sum (b.blog_post_id)
                    from blog_tag t inner join
                    blog_post_blog_tag_rel b on t.id = b.blog_tag_id
                    group by name"""
            self._cr.execute(query)
            n = 0
            for tag_id, k in self._cr.fetchall():
                        