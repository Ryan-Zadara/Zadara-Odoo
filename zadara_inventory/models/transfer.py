# -*- coding: utf-8 -*-
import copy
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class transfer(models.Model):
    _name = 'zadara_inventory.transfer'
    _description = 'zadara_inventory.transfer'

    
    #transfer_name = fields.Integer(default='1')
    
    move_info = fields.Char(string="Notes")
    
    trackingpo_number = fields.Char(required=True, string="Tracking/PO Number: ", help="Tracking number for transfers, PO number for purchases")
    
    transfer_type = fields.Selection([('Transfer','Transfer'), ('Purchase','Purchase'), ('Internal','Internal')],required=True)
    
    source_location_id = fields.Many2one('zadara_inventory.locations',required=True)
    
    destination_location_id = fields.Many2one('zadara_inventory.locations',required=True)
    
    location_id  = fields.Many2one('zadara_inventory.locations', readonly=True)
   
    product_id = fields.Many2one('zadara_inventory.product',required=True)
    
    product_name = fields.Char(related="product_id.product_name")
    
    serial_number = fields.Char(required=True)
    
    quantity = fields.Integer(required=True)
    
    t_quantity = fields.Integer()
    
    responsible_party = fields.Selection([('Irvine','Irvine'), ('Yokneam','Yokneam')], required=True)
    
    transfer_date = fields.Datetime(default=lambda self: fields.datetime.now())
    
    transfer_tag = fields.Char(readonly=True)

    transfer_source_flag = fields.Char(readonly=True)
    transfer_source_quant = fields.Integer()
    p_tag = fields.Many2one('zadara_inventory.p_tag', string="Product Tag")

    #p_tag = fields.Selection([('New','New'), ('Used','Used'),('Obsolete','Obsolete')])
   
    #check valid, location_id, product_id 

    
    def check_create_all(self,q):
        if q != 1:
            raise UserError("bad quantity")
    
    #tests to run object exists 
    #quantity is avalibale 
    #if item is no serialnumber track 
        # if item exists at location update quantity 
        #else create new quanity at location 
        
    
    
    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            val['t_quantity'] = val.get('quantity')
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
            if val.get('source_location_id') == val.get("destination_location_id"):
               
                raise UserError("source and destination location must be different")
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
                    val['location_id'] = val.get('destination_location_id')
                    val['transfer_tag'] = 'write'
                    #val['transfer_source_flag'] = 'yes'
                   # sq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')]]).quantity
                   # dq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('destination_location_id')]]).quantity
                   # val['transfer_source_quant'] = 0 
                    #do stuff here
                else:
                    #raise UserError(val.get("destination_location_id"))
                    raise UserError("bad no product found")
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
                    val['quantity'] = other_quantity + val.get('quantity') 
                    val['location_id'] = val['destination_location_id']
                    val['transfer_tag'] = 'write'
            
            
            if val.get('p_tag') == False and track:
                val['p_tag'] = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')]]).p_tag
                if not self.p_tag.p_tag_type == 'Obsolete' or not self.p_tag.p_tag_type == 'Broken No Warranty':
                    if self.env['zadara_inventory.locations'].search([['id','=',val.get('source_location_id')]]).location_type == 'Customer':
                        val['p_tag'] = self.env['zadara_inventory.p_tag'].search([['name','=','Used']]).id
        
            
        res = super(transfer, self).create(vals_list)
        for vals in vals_list:
           # if self.env['zadara_inventory.product'].search([['id','=',vals.get("product_id")],['product_trackSerialNumber','=',True]]) and vals['transfer_tag'] == 'write':
              #  other_quantity = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', vals.get('product_id')],['location_id','=',vals.get('destination_location_id')]]).quantity
              #  vals['quantity'] = other_quantity + vals.get('quantity') 
              #  vals['location_id'] = vals['destination_location_id']
            #del vals['transfer_name']
          
                #vals['location_id'] = vals['destination_location_id']
            #if vals.get('move_info'):
            del vals['move_info']
            del vals['trackingpo_number']
            del vals['t_quantity']
            del vals['transfer_date']
            del vals['responsible_party']
            del vals['transfer_type'] 
            source_vals = copy.deepcopy(vals)
            del vals['destination_location_id']
            if vals.get("transfer_source_flag") == 'yes':
                #temp = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')]])
                source_vals['location_id'] = source_vals.get('source_location_id')
                source_vals['source_location_id'] = source_vals.get('destination_location_id')
                source_vals['quantity'] = source_vals.get('transfer_source_quant')
               # del source_vals['source_location_id']
                del source_vals['transfer_source_quant']
                del source_vals['transfer_source_flag']
                del source_vals['transfer_tag']
                del source_vals['destination_location_id']
                #raise UserError(source_vals.get('quantity'))
                self.write_to_mitwo(source_vals)
                
              
            del vals['transfer_source_quant']
            del vals['transfer_source_flag']
            
            if vals.get('transfer_tag') == 'write':
                del vals['transfer_tag']  
             
                if self.env['zadara_inventory.product'].search([['id','=',vals.get("product_id")],['product_trackSerialNumber','=',True]]):
                    self.write_to_mi(vals)
                else:
                    e = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')],['location_id','=',val.get('destination_location_id')]])
                    self.write_to_mitwo(vals)
            else:
                del vals['source_location_id']
                del vals['transfer_tag']
               
                self.create_to_mi(vals)
        return res
    
   
    #def set_loc_quant(self):
    def write_to_mitwo(self, vals_list):
        x = vals_list.get('product_id')
        sn = vals_list.get('serial_number')
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', x], ['serial_number', '=', sn],['location_id','=',vals_list.get('location_id')]])
       
        #raise UserError(mi.product_id)
        del vals_list['source_location_id']#if self.env['zadara_inventory.product'].search([['id','=',vals_list.get("product_id")],['product_trackSerialNumber','=',True]]):
        mi.write(vals_list)
        if vals_list.get('p_tag'):
            del vals_list['p_tag']
        self.env['zadara_inventory.product_history'].recurcreate(vals_list)
        #else:
          #  mi.search([['product_id.id', '=', x], ['serial_number', '=', sn],['location_id.id','=',vals_list.get('location_id')]])
          
  
    def write_to_mi(self, vals_list):
        x = vals_list.get('product_id')
        sn = vals_list.get('serial_number')
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', x], ['serial_number', '=', sn],['location_id','=',vals_list.get('source_location_id')]], limit=1)
        mi.location_id = vals_list.get('location_id')
        #raise UserError(mi.product_id)
        del vals_list['source_location_id']#if self.env['zadara_inventory.product'].search([['id','=',vals_list.get("product_id")],['product_trackSerialNumber','=',True]]):
        mi.write(vals_list)
        if vals_list.get('p_tag'):
            del vals_list['p_tag']
        self.env['zadara_inventory.product_history'].create(vals_list)
        #else:
          #  mi.search([['product_id.id', '=', x], ['serial_number', '=', sn],['location_id.id','=',vals_list.get('location_id')]])
        
        
       # raise UserError(mi.id)
        return 
    

  
    @api.model
    def create_to_mi(self, vals_list):
        
        x = self
        new_addition = x.env['zadara_inventory.master_inventory'].create(vals_list)
       # if vals_list.get('p_tag'):
         #   del vals_list['p_tag']
        self.env['zadara_inventory.product_history'].create(vals_list)
        
    

    
    
                   #     sq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('source_location_id')]]).quantity
                #    dq = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['location_id','=',val.get('destination_location_id')]]).quantity
                 #   val['transfer_source_quant'] =#