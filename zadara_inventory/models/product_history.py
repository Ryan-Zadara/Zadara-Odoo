# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class product_history(models.Model):
    _name = 'zadara_inventory.product_history'
    _description = 'zadara_inventory'
    
    mi_id = fields.Many2one('zadara_inventory.master_inventory')
    
    mi_product_id = fields.Many2one(related="mi_id.product_id")
    
    serial_number = fields.Char(related="mi_id.serial_number")
   # @api.onchange('mi_id')
    #def get_pid(self):
     #   self.mi_product_id = self.mi_id.product_id
    
    location_id  = fields.Many2one('zadara_inventory.locations')
    quantity = fields.Integer()
    date_ = fields.Datetime(default=datetime.now())
    
    @api.model
    def create(self,vals_list): 
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', vals_list.get('product_id')], ['serial_number', '=', vals_list.get('serial_number')],['location_id','=',vals_list.get('location_id')]])
        if vals_list.get('product_id'):
            del vals_list['product_id']
        #if vals_list.get('quantity'):
        #    del vals_list['quantity']
        if vals_list.get('serial_number'):
            del vals_list['serial_number']
  
        mi = mi.id
        date__ = datetime.now()
        vals_list.update({'date_':date__})
        vals_list.update({'mi_id':mi})
        res = super(product_history, self).create(vals_list)
        return res
        
        