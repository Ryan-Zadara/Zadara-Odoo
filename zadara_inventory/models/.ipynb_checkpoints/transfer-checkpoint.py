# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class transfer(models.Model):
    _name = 'zadara_inventory.transfer'
    _description = 'zadara_inventory.transfer'

    transfer_name = fields.Char()
    
    transfer_type = fields.Char()
    
    source_location_id = fields.Many2one('zadara_inventory.locations')
    
    destination_location_id = fields.Many2one('zadara_inventory.locations')
    
    location_id  = fields.Many2one('zadara_inventory.locations', readonly=True)
   
    product_id = fields.Many2one('zadara_inventory.product')
    
    product_name = fields.Char(related="product_id.product_name")
    
    serial_number = fields.Char()
    
    quantity = fields.Integer()

    
    #check valid, location_id, product_id 

    
    def check_create_qu(self,q):
        if q == 0:
            raise UserError("bad")
    
    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            q = val.get('quantity')
            self.check_create_qu(q)
            
        res = super(transfer, self).create(vals_list)
        for vals in vals_list:
            del vals["transfer_name"]
            #del vals["product_name"]
            vals['location_id'] = vals['destination_location_id']
            del vals['destination_location_id']
            del vals['source_location_id']
            del vals['transfer_type']
            self.write_to_mi(vals)
        return res
    
   
  
  
    def write_to_mi(self, vals_list):
        x = vals_list.get('product_id')
        sn = vals_list.get('serial_number')
        domain = [('product_id','=', x)]
     
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', x], ['serial_number', '=', sn]])
  
        return mi.write(vals_list)
    
        
  
    
    
    #def write(self,vals_list):
    #    if self.serial_number == '1':
    #        self.serial_number = 'none'
    #    res = super(update_quantity, self).write(vals_list)
    #    for vals in vals_list:
    #        del vals["transfer_name"]
    #        del vals["product_name"]
    #        self.create_to_mi(vals)
    #    return res
   