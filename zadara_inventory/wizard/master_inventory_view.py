# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime

from odoo.exceptions import ValidationError , UserError


class master_inventory_view(models.TransientModel):
    _name = 'zadara_inventory.master_inventory_view'
    _description = 'Stock Quantity History'
    
    location_id = fields.Many2one('zadara_inventory.locations')
 
   # by_location = fields.Boolean()
    at_date = fields.Date(default=lambda self: fields.datetime.now())
   
       
    
    bool_at_date = fields.Date(default=lambda self: fields.datetime.now())
    
   # @api.onchange('at_date')
    #def chng_b(self):
     #   if self.at_date == :
      #      self.bool_at_date = True
       # else:
           # raise UserError(datetime.today())
        #    self.bool_at_date = False
    

        
    
    def calc_qmi(self): 
        mi_t = self.env['zadara_inventory.master_inventory'].search([])
        products = self.env['zadara_inventory.product'].search([])
        #temp_all = self.env['zadara_inventory.product']
        start_date = self.at_date.strftime('%Y-%m-%d')
        end_date = self.bool_at_date.strftime('%Y-%m-%d')
        
        
        if start_date == end_date:
            if self.location_id:
                for p in products: 
                    p.total_quantity = mi_t.return_tq_wl(p.id,self.location_id)
                    p.locat_loc_id = self.location_id.name
            else:
                for p in products: 
                    p.total_quantity = mi_t.return_tq(p.id)
        else:
            all = self.env['zadara_inventory.product_history'].browse([])
            if not self.location_id:
                for x in mi_t:
                    updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.at_date],['product_id.id','=',x.product_id.id],['location_id','=',x.location_id.id],['serial_number','=',x.serial_number]),order="date_ desc", limit=1)

                    all = all | updates
            else:
                for x in mi_t:
                    updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.at_date],['product_id.id','=',x.product_id.id],['location_id.id','=',self.location_id.id],['serial_number','=',x.serial_number]),order="date_ desc", limit=1)
                    all = all | updates
            for p in products: 
                p.total_quantity = all.ph_return_tq(p.id)
                p.locat_loc_id = self.location_id.name
       
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
            
        
    
    