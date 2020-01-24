# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class update_quantity(models.Model):
    _name = 'zadara_inventory.update_quantity'
    _description = 'zadara_inventory.upadate_quantity'

    update_quantity_name = fields.Char()
    
    location_id = fields.Many2one('zadara_inventory.locations')
    
    product_id = fields.Many2one('zadara_inventory.product')
    
    product_name = fields.Char(related="product_id.product_name")
    
    serial_number = fields.Char()
    
    quantity = fields.Integer()

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
        if q != 1 or q != 0:
            raise UserError("bad")
    
    def pre_checks(self,q):
        if q < 0:
            raise UserError("quantitys cannot be negetive")
        
    
    @api.model_create_multi
    def create(self,vals_list):
        track = 0
        for val in vals_list:
            q = val.get('quantity')
            self.pre_checks(q)
            x = self.env['zadara_inventory.product'].search_count([['product_id', '=', val.get('product_id')], ['product_trackSerialNumber', '=', True]])
            if self.env['zadara_inventory.product'].search([['product_id', '=', val.get('product_id')], ['product_trackSerialNumber', '=', True]]):
                raise UserError("break")
                if val.get('serial_number') == "" or val.get('serial_number') == 'N/A':
                    raise UserError('bad sn line')
                te = self.env['zadara_inventory.master_inventory'].search(['serial_number', '=', val.get('serial_number')]) 
                if self.env['zadara_inventory.master_inventory'].browse(te).contains(val.get('product_id')):
                    raise UserError("bad sn line ")
            raise UserError(self.product_id.product_id.id)  
                
            track = track +1
        res = super(update_quantity, self).create(vals_list)
        for vals in vals_list:
            del vals["update_quantity_name"]
            #del vals["product_name"]
            self.create_to_mi(vals)
        return res
    
   
  
    @api.model
    def create_to_mi(self, vals_list):
        new_addition = self.env['zadara_inventory.master_inventory'].create(vals_list)

    
    
    def write(self,vals_list):
        if self.serial_number == '1':
            self.serial_number = 'none'
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
    
    
    
    