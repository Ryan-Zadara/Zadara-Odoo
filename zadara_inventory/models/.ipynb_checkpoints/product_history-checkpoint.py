# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError , UserError

class product_history(models.Model):
    _name = 'zadara_inventory.product_history'
    _description = 'zadara_inventory'
    
    mi_id = fields.Many2one('zadara_inventory.master_inventory')
    
    product_id = fields.Many2one("zadara_inventory.product")
    
    serial_number = fields.Char()
   # @api.onchange('mi_id')
    #def get_pid(self):
     #   self.mi_product_id = self.mi_id.product_id
    total_quantity = fields.Char()
    location_id  = fields.Many2one('zadara_inventory.locations')
    quantity = fields.Integer()
    date_ = fields.Datetime(default=lambda self: fields.datetime.now())
    t_quantity = fields.Integer()
    
    def if_date(self,date,test_date):
        if date <= test_date:
            return True 
        else:
            return False 
    
    def ph_return_tq(self,p_id):
        tot = 0
        for x in self: 
            if x.product_id.id == p_id:
                #raise UserError(p_id)         
                tot = tot + x.quantity 
        return tot
    
    def ph_return_tq_wl(self,p_id,l_id):
        tot = 0
       
        for x in self: 
            #raise UserError(l_id)
            if x.product_id.id == p_id and x.location_id.id == l_id:
                       
                tot = tot + x.quantity 
                
        return tot
    
    
    
    
    
    
    
    
    def recurcreate(self,vals_list):
         #for x in self:
        self.create(vals_list)
    @api.model
    def create(self,vals_list): 
       
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', vals_list.get('product_id')], ['serial_number', '=', vals_list.get('serial_number')],['location_id','=',vals_list.get('location_id')]])

        # if vals_list.get('product_id'):
           #     del vals_list['product_id']
            #if vals_list.get('quantity'):
            #    del vals_list['quantity']
          #  if vals_list.get('serial_number'):
          #      del vals_list['serial_number']
            #raise UserError("asdkjf;a")
        mi = mi.id
        date__ = datetime.now()
        vals_list.update({'date_':date__})
        vals_list.update({'mi_id':mi})
        res = super(product_history, self).create(vals_list)
        return res
        
        