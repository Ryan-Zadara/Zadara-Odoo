# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class master_inventory(models.Model):
    _name = 'zadara_inventory.master_inventory'
    _description = 'zadara_inventory.master_inventory'
   # name = fields.Char()
    
    

    
    product_id = fields.Many2one('zadara_inventory.product')
    
    location_id = fields.Many2one('zadara_inventory.locations')                             
    
    serial_number = fields.Char()
    #inv_product_sn = fields.Many2one('zadara_inventory.serialnumbers')#compute="compute_sn")#compute="compute_sn", inverse="inv_compute_sn")
    
    quantity = fields.Integer()
    #product_ids = inv_product.ids
  

    #def check_invforsn(self,pid,sn):
     #   for i in self:
    #        if i.product_id == pid:
      #          if i.serial_number == sn:
       #             return True
        #        raise ValidationError(pid) 
        
    @api.model_create_multi
    def create(self,vals_list):
        res = super(master_inventory, self).create(vals_list)
        return res
    
    def get_recordset(self, pids):
        rset = self.env.ref(pids,['zadara_inventory.master_inventory'])
        return rset                 
                             
                             
    def write(self,vals_list):
        res = super(master_inventory, self).write(vals_list)
        return res
        
                