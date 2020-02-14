# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class product_number(models.Model):
    _name = 'zadara_inventory.vendors'
    _description = 'zadara_inventory.vendors'
    
    #product_id = fields.Many2one('zadara_inventory.product')
    
    name = fields.Char(string="Vendor Name", help="Does NOT have to match Location name")
    
    short_name = fields.Char(help='Nickname')
    
    location_id = fields.Many2one('zadara_inventory.locations')
    
 