# -*- coding: utf-8 -*-

from odoo import fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError , UserError


class inv_report_calc(models.TransientModel):
    _name = 'zadara_inventory.inv_report_calc'
    _description = 'Stock Quantity History'
    
    inv_at_date = fields.Datetime(default = datetime.now())
    
   
    location_id = fields.Many2one('zadara_inventory.locations')
    
    add_serial_number = fields.Boolean()
        
    def calc_at_date(self):
        #if self.locations == None:
            #location_id = self.env['zadara_inventory.product_history'].get.context('product_history')
        
        products = self.env['zadara_inventory.product'].search([])
        all = self.env['zadara_inventory.product_history']
       # for_search  = self.env['zadara_inventory.product_history'].search([])
        mi_t = self.env['zadara_inventory.master_inventory'].search([])
        if not self.location_id:
            for x in mi_t:
                updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['product_id','=',x.product_id.id],['serial_number','=',x.serial_number]),order="date_ desc", limit=1)
                all = updates | all 
        else:
            for x in mi_t:
                updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['mi_id.product_id','=',x.product_id.id],['mi_id.serial_number','=',x.serial_number],['location_id','=',self.location_id.id]),order="date_ desc", limit=1)
                #updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['mi_id.product_id','=',x.id],['location_id','=',self.location_id.id]),order="date_ asc", limit=1)
                all = updates | all 
        
       
        for x in all:
            unt = self.env['zadara_inventory.master_inventory'].search([])
            count = unt.return_tq(x.product_id.id)
           # raise UserError(count)
            
            x.total_quantity = count
        
        if not self.add_serial_number:
            cop = self.env['zadara_inventory.product_history']
            for x in all:
                if not x.product_id in cop.product_id:
                    cop = cop | x
            all = cop
        
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
            
        
    
    