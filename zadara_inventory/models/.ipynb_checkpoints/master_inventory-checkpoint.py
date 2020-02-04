# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError , UserError

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
        
    #def get_tot_qunant(self,product_):
        #q = self.env['zadara_inventory.product'].search([''])
       # for x in 
        #    raise UserError(x)
        
        #    i = i + x.quantity
      #  return 1
    @api.model
    def create(self,vals_list):
  
        res = super(master_inventory, self).create(vals_list)
        vals_list.update({'mi_id':self.id})
        #self.env['zadara_inventory.product_history'].create(vals_list)
        
        #f = self.env['zadara_inventory.product']
        
        #f.compute_quantity(vals_list.get('product_id'))
        return res
    
    def get_recordset(self, pids):
        rset = self.env.ref(pids,['zadara_inventory.master_inventory'])
        return rset                 
    
    def return_tq(self,p_id):
       
        tot = 0
       # raise UserError(self)
        for x in self: 
            
            if x.product_id.id == p_id:
                #raise UserError(p_id)
                tot = tot + x.quantity 
                
               
        return tot
                         
    def write(self,vals_list):
        
        res = super(master_inventory, self).write(vals_list)
       # x = self.
        vals_list.update({'mi_id':self.id})
        self.env['zadara_inventory.product_history'].create(vals_list)
       # self.env['zadara_inventory.product'].search(['id','=',vals_list.get('product_id')]).compute_quantity()
        return res
        
        
   
        