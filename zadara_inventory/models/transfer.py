# -*- coding: utf-8 -*-
import copy
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class transfer(models.Model):
    _name = 'zadara_inventory.transfer'
    _description = 'zadara_inventory.transfer'

    
    transfer_name = fields.Integer(compute="comp_tn",store=True, default=lambda self: self.env['zadara_inventory.transfer'].comp_tn())
    
    
    transfer_type = fields.Selection([('Transfer','Transfer'), ('Purchase','Purchase')],required=True)
    
    source_location_id = fields.Many2one('zadara_inventory.locations',required=True)
    
    destination_location_id = fields.Many2one('zadara_inventory.locations',required=True)
    
    location_id  = fields.Many2one('zadara_inventory.locations', readonly=True)
   
    product_id = fields.Many2one('zadara_inventory.product',required=True)
    
    product_name = fields.Char(related="product_id.product_name")
    
    serial_number = fields.Char(required=True)
    
    quantity = fields.Integer(required=True)
    
    responsible_party = fields.Selection([('Irvine','Irvine'), ('Yoknaem','Yoknaem')], required=True)
    
    transfer_date = fields.Datetime(default=datetime.now())
    
    transfer_tag = fields.Char(readonly=True)

    transfer_source_flag = fields.Char(readonly=True)
    transfer_source_quant = fields.Integer()
    def comp_tn(self):
        x = self.env['zadara_inventory.transfer'].search([],order="transfer_name desc", limit=1)
        r = x.transfer_name + 1
        self.tranfser_name = r
        return r
    
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
            val['transfer_source_flag'] = "no"
            val['transfer_source_quant'] = 0
            #if val.get('quantity') < 0:
            #    raise UserError("quantity cannot be less than zero")
            #if not val.get('source_location_id'):
            #    raise UserError("no source location")
            #if not val.get('destination_location_id'):
            #    raise UserError("no destination location")
            #if not val.get('product_id'):
            #    raise UserError("no product")
            #if val.get('reponsible_party') == '':
            #    raise UserError("no responsible party")
            if not val.get('transfer_date'):
                val['transfer_date'] = datetime.now()
            track = self.env['zadara_inventory.product'].search([['id','=',val.get("product_id")],['product_trackSerialNumber','=',True]])
            
            if track:            
                #q = val.get('quantity')
                #if not q:
                #    raise UserError('bad sn line')
                self.check_create_all(val.get('quantity')) 
                if val.get('serial_number') == 'N/A':
                    raise UserError('bad sns')
                
                if self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')],['quantity','=',val.get('quantity')]]) and val.get('quantity') == 1:
                    val['location_id'] = val['destination_location_id']
                    val['transfer_tag'] = 'write'
                    #val['transfer_source_flag'] = 'yes'
                   # sq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')]]).quantity
                   # dq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('destination_location_id')]]).quantity
                   # val['transfer_source_quant'] = 0 
                    #do stuff here
                else:
                    raise UserError(val.get('serial_number'))
            else:

                if val.get('serial_number') != 'N/A':
                    val['serial_number'] = 'N/A'                
                sq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')]]).quantity
                 # find prodcut location and and check if quantity is > quantity 
                resour = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')],['location_id','=',val.get('source_location_id')]])
                if resour:

                        #val['quantity'] = val['quantity']
                    val['transfer_source_flag'] = 'yes'
                    val['transfer_source_quant'] = sq - val.get('quantity')
                
                if sq < val.get('quantity'):
                    #raise UserError("not enough inventory at source location")
                    raise UserError(sq)
                if not self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')],['location_id','=',val.get('destination_location_id')]]):

                    val['location_id'] = val['destination_location_id']
                    val['transfer_tag'] = 'create'
                    
                else:
                    other_quantity = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')],['location_id','=',val.get('destination_location_id')]]).quantity
                    val['quantity'] = other_quantity + val['quantity'] 
                    val['location_id'] = val['destination_location_id']
                    val['transfer_tag'] = 'write'
                
            
            
            
            
        res = super(transfer, self).create(vals_list)
        for vals in vals_list:
            #del vals['transfer_name']
          
                #vals['location_id'] = vals['destination_location_id']
           
            del vals['destination_location_id']
           
            del vals['transfer_date']
            del vals['responsible_party']
            del vals['transfer_type'] 
            source_vals = copy.deepcopy(vals)
            if vals.get("transfer_source_flag") == 'yes':
                #temp = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')]])
                source_vals['location_id'] = source_vals.get('source_location_id')
                source_vals['quantity'] = source_vals.get('transfer_source_quant')
                del source_vals['source_location_id']
                del source_vals['transfer_source_quant']
                del source_vals['transfer_source_flag']
                del source_vals['transfer_tag']
                self.write_to_mi(source_vals)
                
            del vals['transfer_source_quant']
            del vals['transfer_source_flag']
            del vals['source_location_id']
            if vals.get('transfer_tag') == 'write':
                del vals['transfer_tag'] 
                
                self.write_to_mi(vals)
            else:
                del vals['transfer_tag']
                self.create_to_mi(vals)
        return res
    
   
    #def set_loc_quant(self):
        
  
    def write_to_mi(self, vals_list):
        x = vals_list.get('product_id')
        sn = vals_list.get('serial_number')
     
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', x], ['serial_number', '=', sn],['location_id','=',vals_list.get('location_id')]])
  
        return mi.write(vals_list)
    

  
    @api.model
    def create_to_mi(self, vals_list):
        new_addition = self.env['zadara_inventory.master_inventory'].create(vals_list)
    

    
    
                   #     sq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')]]).quantity
                #    dq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('destination_location_id')]]).quantity
                 #   val['transfer_source_quant'] =#