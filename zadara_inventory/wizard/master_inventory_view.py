# -*- coding: utf-8 -*-

from odoo import fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError , UserError


class master_inventory_view(models.TransientModel):
    _name = 'zadara_inventory.master_inventory_view'
    _description = 'Stock Quantity History'
    
   
   
    location_id = fields.Many2one('zadara_inventory.locations')
    
   # add_serial_number = fields.Boolean()
        
    def calc_qmi(self):
        #if self.locations == None:
            #location_id = self.env['zadara_inventory.product_history'].get.context('product_history')
        mi_x = self.env['zadara_inventory.master_inventory'].search([])
        products = self.env['zadara_inventory.product'].search([])
        all = self.env['zadara_inventory.master_inventory']
       # for_search  = self.env['zadara_inventory.product_history'].search([])
        mi_t = self.env['zadara_inventory.master_inventory']
        if not self.location_id:
            for y in products:
                
                for x in mi_x:
                    if not y < mi_x:
                        all = all | x 

                    
        else:
            if not self.location_id:
                for y in products:
                    y.total_quantity = 0 
                    t = self.env['zadara_inventory.master_inventory'].search(['product_id','=',y],['location_id','=',location_id])
                    eas = 0
                    for x in t:
                        ease = ease + x.quantity 
                    all = all | t
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
            
        
    
    