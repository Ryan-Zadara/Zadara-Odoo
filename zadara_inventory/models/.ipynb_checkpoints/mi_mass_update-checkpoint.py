# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError , UserError

class mi_mass_update(models.Model):
    _name = 'zadara_inventory.mi_mass_update'
    _description = 'zadara_inventory.mi_mass_update'
    
   
    
    serialnumber = fields.Char()
    
    location_id = fields.Many2one('zadara_inventory.locations')                             
    
    quantity = fields.Integer()
    product_number = fields.Many2one('zadara_inventory.product_number')
    
    
    
    @api.model_create_multi
    def create(self,vals_list):
        for x in vals_list:
            raise UserError("stop")
        #if x.get('')