# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class info(models.Model):
    _name = 'zadara_inventory.info'
    _description = 'zadara_inventory.info'
    
    product_id = fields.Many2one('zadara_inventory.product')
    
    mi_id = fields.Many2one('zadara_inventory.master_inventory')
    
    