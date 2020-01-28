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
    
    transfer_tag = fields.Char(readonly=True)

    
    #check valid, location_id, product_id 

    
    def check_create_all(self,q):
        if q != 1:
            raise UserError("bad")
    
    #tests to run object exists 
    #quantity is avalibale 
    #if item is no serialnumber track 
        # if item exists at location update quantity 
        #else create new quanity at location 
        
    
    
    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:

            if not val.get('source_location_id'):
                raise UserError("no source location")
            if not val.get('destination_location_id'):
                raise UserError("no destination location")
            if not val.get('product_id'):
                raise UserError("no product")
            track = self.env['zadara_inventory.product'].search([['id','=',val.get("product_id")],['product_trackSerialNumber','=',True]])
            
            if track:            
                q = val.get('quantity')
                if not q:
                    raise UserError('bad sn line')
                self.check_create_all(q) 
                if val.get('serial_number') == 'N/A':
                    raise UserError('bad sns')
                if self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')],['quantity','=',val.get('quantity')]]):
                    del val["transfer_name"]
                    #del vals["product_name"]
                    val['location_id'] = val['destination_location_id']
                    del val['destination_location_id']
                    del val['source_location_id']
                    del val['transfer_type']
                    val['transfer_tag'] = 'write'
                    #do stuff here
                else:
                    raise UserError('couldnt find that product with that serial number')
            else:
                if val.get('serial_number') != 'N/A':
                    val['serial_number'] = 'N/A'
                 # find prodcut location and and check if quantity is > quantity 
                if not self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')],['location_id','=',val.get('destination_location_id')],['quantity','>=',val.get('quantity')]]):
                    raise UserError("bad at location")
                if not self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')],['location_id','=',val.get('destination_location_id')]]):
                
                    val['location_id'] = val['destination_location_id']
                    del val['destination_location_id']
                    del val['source_location_id']
                    del val['transfer_type']
                    del val["transfer_name"]
                    val['transfer_tag'] = 'create'
                else:
                    other_quantity = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')],['location_id','=',val.get('source_location_id')]]).get('quantity')
                    val['quantity'] = other_quantity - quantity 
                    val['location_id'] = val['destination_location_id']
                    del val['destination_location_id']
                    del val['source_location_id']
                    del val['transfer_type']
                    del val["transfer_name"]
                    val['transfer_tag'] = 'write'
            
        res = super(transfer, self).create(vals_list)
        for vals in vals_list:
            if vals.get('transfer_tag') == 'write':
                #del vals["transfer_name"]
                #del vals["product_name"]
                #vals['location_id'] = vals['destination_location_id']
                #del vals['destination_location_id']
                #del vals['source_location_id']
                #del vals['transfer_type']
                self.write_to_mi(vals)
            else:
                self.create_to_mi(vals)
        return res
    
   
  
  
    def write_to_mi(self, vals_list):
        x = vals_list.get('product_id')
        sn = vals_list.get('serial_number')
     
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', x], ['serial_number', '=', sn]])
  
        return mi.write(vals_list)
    

  
    @api.model
    def create_to_mi(self, vals_list):
        new_addition = self.env['zadara_inventory.master_inventory'].create(vals_list)
    
    #def write(self,vals_list):
    #    if self.serial_number == '1':
    #        self.serial_number = 'none'
    #    res = super(update_quantity, self).write(vals_list)
    #    for vals in vals_list:
    #        del vals["transfer_name"]
    #        del vals["product_name"]
    #        self.create_to_mi(vals)
    #    return res
   