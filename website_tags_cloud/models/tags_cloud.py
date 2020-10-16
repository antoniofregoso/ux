# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#


from odoo import api, fields, models

class TagsCloudTag(models.Model):    
    _name = 'tags_cloud.tag'
    _description = 'Tags Cloud Tag'
    _order = 'percentile asc, name asc'
    
    name = fields.Char('Name' , required=True)
    percentile = fields.Integer('Percentile', defautl=50, required=True)
    url = fields.Char('URL')
    tags_cloud_id = fields.Many2one('tags_cloud.tags_cloud', string="Tags Cloud", ondelete='cascade', required=True)
    style = fields.Char('Style')
    
class TagsCloud(models.Model):  
    _name = 'tags_cloud.tags_cloud'
    _description = 'Tags Cloud'
    _inherit = ['website.multi.mixin']
    
    name = fields.Char('Name' , required=True)
    website_id = fields.Many2one('website', help='Website where it will be located.')
    font_h1 = fields.Integer('Font Min Height', default=8, required=True, help='Minimun height')
    font_h2 = fields.Integer('Font Max Height', default=24, required=True, help="Maximum height")
    start = fields.Char('Start', default="#2200ff", help='color of the smallest font, if options.color = "gradient"')
    end = fields.Char('End', default="#ee0000", help='color of the largest font, if options.color = "gradient"')
    color = fields.Selection([('gradient', 'Gradient'), ('random-light', 'Random Light'), ('random-dark', 'Random Dark')], string='Color', default='gradient', required=True)
    rotation_ratio = fields.Selection(
        [('0', '0'), ('0.1', '0.1'), ('0.2', '0.2'), ('0.3', '0.3'), ('0.4', '0.4'), ('0.5', '0.5'), ('0.6', '0.6'), ('0.7', '0.7'), ('0.8', '0.8'), ('0.9', '0.9'), ('1', '1')], 
        string = 'Rotation', default = '0.3', help ='0 is all horizontal, 1 is all vertical', required=True)    
    sort =  fields.Selection([('highest','Highest'), ('lowest','Lowest'), ('random','Random')], string='Sort', default='lowest', help=' "highest" to show big words first, "lowest" to do small words first, "random" to not care', required=True)
    shape = fields.Selection([('circle','Circle'), ('square','Square'), ('diamond','Diamond'), ('triangle','Triangle'), ('triangle-forward','Triangle Forward'), ('x','X'), ('pentagon','Pentagon'), ('star','Star')], string='Shape', default='circle', required=True)
    tags_ids = fields.One2many('tags_cloud.tag', 'tags_cloud_id', 'Tags')
    
    
