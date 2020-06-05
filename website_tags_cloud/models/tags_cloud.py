# -*- coding: utf-8 -*-


from odoo import api, fields, models

class TagsCloudItem(models.Model):    
    _name = 'tags_cloud.item'
    _description = 'Tags Cloud Item'
    _order = 'percentile asc, name asc'
    
    name = fields.Char('Name' , required=True)
    percentile = fields.Integer('Percentile', defautl=50, required=True)
    url = fields.Char('URL')
    tags_cloud_id = fields.Many2one('tags_cloud.tags_cloud', string="Tags Cloud", ondelete='cascade', required=True)
    
class TagsCloud(models.Model):  
    _name = 'tags_cloud.tags_cloud'
    _description = 'Tags Cloud'
    
    name = fields.Char('Name' , required=True)
    background = fields.Char('Background', default="#ffffff", required=True)
    transparency = fields.Selection(
        [('0','0'), ('25','1'), ('51','2'), ('77','3'), ('102','4'), ('128','5'), ('153','6'), ('179','7'), ('204','8'), ('230','9'), ('255','10')], string = 'transparency', default='0', required=True, help='0 transparent, 10 solid')
    start = fields.Char('Start', default="#2200ff", help='color of the smallest font, if options.color = "gradient"')
    end = fields.Char('End', default="#ee0000", required=True, help='color of the largest font, if options.color = "gradient"')
    color = fields.Selection([('gradient', 'Gradient'), ('random-light', 'Random Light'), ('random-dark', 'Random Dark')], string='Color', default='gradient', required=True)
    rotation_ratio = fields.Selection(
        [('0', '0'), ('0.1', '0.1'), ('0.2', '0.2'), ('0.3', '0.3'), ('0.4', '0.4'), ('0.5', '0.5'), ('0.6', '0.6'), ('0.7', '0.7'), ('0.8', '0.8'), ('0.9', '0.9'), ('1', '1')], 
        string = 'Rotation', default = '0.3', help ='0 is all horizontal, 1 is all vertical', required=True)
    print_multiplier = fields.Selection([('1', '1'),('2', '2'), ('3', '3')], string='Print Multiplier', default='1', help='set to 3 for nice printer output; higher numbers take longer', required=True)
    sort =  fields.Selection([('highest','Highest'), ('lowest','Lowest'), ('random','Random')], string='Sort', default='highest', help=' "highest" to show big words first, "lowest" to do small words first, "random" to not care', required=True)
    shape = fields.Selection([('circle','Circle'), ('square','Square'), ('diamond','Diamond'), ('triangle','Triangle'), ('triangle-forward','Triangle Forward'), ('x','X'), ('pentagon','Pentagon'), ('star','Star')], string='Shape', default='circle', required=True)
    tags_ids = fields.One2many('tags_cloud.item', 'tags_cloud_id', 'Tags')
    
    
