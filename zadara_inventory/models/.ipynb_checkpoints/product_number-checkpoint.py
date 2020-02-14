# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class product_number(models.Model):
    _name = 'zadara_inventory.product_number'
    _description = 'zadara_inventory.product_number'
    
    product_id = fields.Many2one('zadara_inventory.product')
    
    name = fields.Char(string="Product Number")
    
    
    