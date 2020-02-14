# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime

from odoo.exceptions import ValidationError , UserError


class q_mi(models.TransientModel):
    _name = 'zadara_inventory.q_mi'
    _description = 'Stock Quantity History'
    
    
 
    by_product = fields.Boolean()

    
   # @api.onchange('at_date')
    #def chng_b(self):
     #   if self.at_date == :
      #      self.bool_at_date = True
       # else:
           # raise UserError(datetime.today())
        #    self.bool_at_date = False
    

        
    
    def qmi(self): 
        mi_t = self.env['zadara_inventory.master_inventory'].search([])
        #products = self.env['zadara_inventory.product'].search([])
        #temp_all = self.env['zadara_inventory.product']
       # start_date = self.at_date.strftime('%Y-%m-%d')
       # end_date = self.bool_at_date.strftime('%Y-%m-%d')
       # for x in mi_t:
            
        all = self.env['zadara_inventory.master_inventory']
        
        all = mi_t
        
        unt = all
        #if self.by_location:
        h = self.env['zadara_inventory.master_inventory']
        for x in all:     
           # raise UserError(x.product_id.id)
            if h.product_id.id == x.product_id.id and h.location_id.id == x.location_id.id and x.serial_number != 'N/A':
                if self.by_product:
                    all = all - x 
                else:
                    x.report_q_mi = h.report_q_mi
                    h = x 
                    
            else:    
                count = unt.return_tq_wl(x.product_id.id,x.location_id.id)
            
                #raise UserError(count)
            
                x.report_q_mi = count
                h = x
        #raise UserError(all)
              
            #temp3 = self.env['zadara_inventory.product_history']
        if self.by_product:
            temp2 = all #self.env['zadara_inventory.product_history'].search(['ids','in',all.ids])
                #self.env['zadara_inventory.product_history'].browse(all)
                #temp2 = 
            temp = all

            for x in temp2: 
                for y in all:  

                    if y.product_id.id == x.product_id.id and y.location_id.id == x.location_id.id:


                        if x.id != y.id and y.id > x.id:
                            all = all - y
        
        
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
            'res_model': 'zadara_inventory.master_inventory',
            
            'domain': [['id','in',all.ids]],
        }
        return action
       
        
       # master = updates.get.context()
        
        #for x in updates and y in transfers:
        #    product = x.context.get('product_id')
            
        
    
    