# -*- coding: utf-8 -*-

from odoo import fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError , UserError


class master_inventory_view(models.TransientModel):
    _name = 'zadara_inventory.master_inventory_view'
    _description = 'Stock Quantity History'
    
   # at_date = fields.Date(default=datetime.now())
   
    location_id = fields.Many2one('zadara_inventory.locations')
    
   # add_serial_number = fields.Boolean()
        
    def calc_qmi(self): 
        # for_search  = self.env['zadara_inventory.product_history'].search([])
        #if self.locations == None:
            #location_id = self.env['zadara_inventory.product_history'].get.context('product_history')
      #  mi_x = self.env['zadara_inventory.master_inventory'].search([])
        products = self.env['zadara_inventory.product'].search([])
       
    
        
        
        mi_t = self.env['zadara_inventory.master_inventory'].search([])
        if self.location_id:
            for p in products: 
                p.total_quantity = mi_t.return_tq_wl(p.id,self.location_id)
        else:
            for p in products: 
                p.total_quantity = mi_t.return_tq(p.id)
       # else:
        #    mi_t = self.env['zadara_inventory.product_history'].search(['date_','<=', self.at_date],order="date_ desc", limit=1)
         #   if self.location_id:
          #      for p in products: 
           #         p.total_quantity = mi_t.ph_return_tq_wl(p.id,self.location_id)
           # else:
            #    for p in products: 
             #       p.total_quantity = mi_t.ph_return_tq(p.id)
            
           # raise UserError(p.total_quantity)
            
            #for x in products:
            #    count = 0
            #    x = 0
            #    r = self.env['zadara_inventory.product'].browse(x)
               
            #    for r.id in mi_t:
            #        if x == y.id:
            #            
            #            if x == 0:
                           # all = all | y
                            
            #            x = 1
            #            count = count  + x.quantity
                
            #    r.total_quantity = count
                        
                        
                    

                    
     #   else:
      #      if not self.location_id:
       ##            y.total_quantity = 0 
         #           t = self.env['zadara_inventory.master_inventory'].search(['product_id','=',y],['location_id','=',location_id])
          #          eas = 0
           #         for x in t:
            #            ease = ease + x.quantity 
             #       all = all | t
                #updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['mi_id.product_id','=',x.id],['location_id','=',self.location_id.id]),order="date_ asc", limit=1)
               
          

        
   
        
        action = {
            'type': 'ir.actions.act_window',
            #'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'view_mode': 'tree',
            'name': 'Products',
            'res_model': 'zadara_inventory.product',
            
            'domain': [['id','in',products.ids]],
        }
        return action
       
        
       # master = updates.get.context()
        
        #for x in updates and y in transfers:
        #    product = x.context.get('product_id')
            
        
    
    