# -*- coding: utf-8 -*-

from odoo import fields, models, _
from datetime import datetime


class inv_report_calc(models.TransientModel):
    _name = 'zadara_inventory.inv_report_calc'
    _description = 'Stock Quantity History'
    
    inv_at_date = fields.Datetime(default = datetime.now())
    
   
    
    
        
    def calc_at_date(self):
        #if self.locations == None:
            #location_id = self.env['zadara_inventory.product_history'].get.context('product_history')
        products = self.env['zadara_inventory.product'].search([])
        all = self.env['zadara_inventory.product_history']
        for x in products:
            updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['mi_id.product_id','=',x.id]),order="date_ asc", limit=1)
            all = updates | all 
            
        action = {
            'type': 'ir.actions.act_window',
            #'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'view_mode': 'tree',
            'name': 'Products',
            'res_model': 'zadara_inventory.product_history',
            
            'domain': [['id','in',all.ids]],
        }
        return action
       
        
       # master = updates.get.context()
        
        #for x in updates and y in transfers:
        #    product = x.context.get('product_id')
            
        
    
    