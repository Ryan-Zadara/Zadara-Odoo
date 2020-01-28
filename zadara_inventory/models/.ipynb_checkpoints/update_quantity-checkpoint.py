# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class update_quantity(models.Model):
    _name = 'zadara_inventory.update_quantity'
    _description = 'zadara_inventory.upadate_quantity'

    update_quantity_name = fields.Char()
    
    location_id = fields.Many2one('zadara_inventory.locations')
    
    product_id = fields.Many2one('zadara_inventory.product')
    
    #product_trackSerialNumber = fields.Boolean(related="product_id.product_trackSerialNumber")
    
    product_name = fields.Char(related="product_id.product_name")
    
    serial_number = fields.Char()
    
    quantity = fields.Integer()
    
    #@api.onchange('product_id')
    #def fix_track(self):
    #    self.product_trackSerialNumber = self.product_id.product_trackSerialNumber
    #relation 
    #move = fields.Many2one('zadara_inventory.moves')
    
    #checks procdure valid, location_id, product_id 
    #precheck quatity not <0 
        #1 prpoduct tracking serial number or not 
            #2 if yes 
                #makes sure qunatity is 1, make sure sn is unique and not = to N/A or blank
            #2 if not 
                #make sn = too N/A, see if product exists at location 
                #if yes
                    #write over quantity 
                #if not 
                    #create instance with quantity at 
    def check_create_qu(self,q):
        if q >1 or q < 0:
            raise UserError("bad")
    
    def pre_checks(self,q):
        if q < 0:
            raise UserError("quantitys cannot be negetive")
        
    
    @api.model_create_multi
    def create(self,vals_list):
        
        for val in vals_list:
            if not val.get('product_id'):
                raise UserError("no product")
            q = val.get('quantity')
            self.pre_checks(q)
            track = self.env['zadara_inventory.product'].search([['id','=',val.get("product_id")],['product_trackSerialNumber','=',True]])
            if not val.get('location_id'):
                raise UserError("no location")
            if track:
                if not val.get('serial_number'):
                    raise UserError('bad sn line')
                if val.get('serial_number') == 'N/A':
                    raise UserError('bad sns')                
                if self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')]]):
                    if self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['quantity','!=', val.get('quantity')]]):
                        #del val["product_trackSerialNumber"]
                        del val["update_quantity_name"]
                        return self.write_to_mi(val)
                    elif self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['quantity','=', val.get('quantity')]]):
                        raise UserError("cannot have 2 same serial numbers ")
                self.check_create_qu(q) 
            else:
                val['serial_number'] = "N/A"
                if self.env['zadara_inventory.master_inventory'].search([['location_id','=', val.get('location_id')],['product_id', '=',val.get('product_id')]]):
                    del val["update_quantity_name"]
                    return self.write_to_mi(val)
                
                    
                    
             
                
          
        res = super(update_quantity, self).create(vals_list)
        for vals in vals_list:
            if vals.get('update_quantity_name'):
                del vals["update_quantity_name"]
            #del vals["product_name"]
            self.create_to_mi(vals)
        return res
    
   
  
    @api.model
    def create_to_mi(self, vals_list):
        new_addition = self.env['zadara_inventory.master_inventory'].create(vals_list)

    def write_to_mi(self,vals_list):
        
        x = vals_list.get('product_id')
        sn = vals_list.get('serial_number')
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', x], ['serial_number', '=', sn]])
        
        return mi.write(vals_list)
    
    def write(self,vals_list):
        res = super(update_quantity, self).write(vals_list)
        return res
    # def sn_no_null(self):

        #for i in self:
        #    if i.product_id.sudo().product_trackSerialNumber == True:
        #        if serial_number == None:
        #            raise ValidationError("no sn")
                    
    #check product type 
   # @api.constrains('serial_number')
    #def check_sn(self):
     #   if self.env['zadara_inventory.master_inventory'].check_invforsn(t.product_id,t.serial_number):
      #      raise ValidationError("same sn")
                
    #check serial numbers 
    #create
    
    
    
    