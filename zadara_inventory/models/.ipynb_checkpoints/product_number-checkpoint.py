# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class product_number(models.Model):
    _name = 'zadara_inventory.product_number'
    _description = 'zadara_inventory.product_number'
    
    product_id = fields.Many2one('zadara_inventory.product')
    
    name = fields.Char(string="Product Number")
    
    @api.model_create_multi
    def create(self,vals_list):
        for y in vals_list:
            for x in self.env['zadara_inventory.product_number'].search([]):
                if x.name == y.get('name'):
                    raise UserError("Product Number Already on file")
        res = super(product_number, self).create(vals_list)
        return res
    