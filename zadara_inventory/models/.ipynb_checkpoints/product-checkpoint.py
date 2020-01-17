# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product(models.Model):
    _name = 'zadara_inventory.product'
    _description = 'zadara_inventory.product'

    name = fields.Char()
    product_id = fields.Char()
    part_number = fields.Char()
    product_category = fields.Char()
    
    product_grab = fields.Char() #must be product
    
    product_trackSerialNumber = fields.Boolean()