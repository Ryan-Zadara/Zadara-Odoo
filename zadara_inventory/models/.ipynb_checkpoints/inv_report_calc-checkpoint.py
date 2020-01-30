# -*- coding: utf-8 -*-

from odoo import fields, models, _
from datetime import datetime


class inv_report_calc(models.TransientModel):
    _name = 'zadara_inventory.inv_report_calc'
    _description = 'Stock Quantity History'
    
    inv_at_date = fields.Datetime(default = datetime.now())
    
    products = fields.One2many('zadara_inventory.product_history','product_id')
    
    
        
    def calc_at_date(self):
        if self.products == None:
            products = self.env['zadara_inventory.product_history'].get.context('product_history')
        all = self.env['zadara_inventory.product_history']
        for x in products:
            updates = self.env['zadara_inventory.product_history'].search((['update_date','<=', self.inv_at_date],['product_id','=',x]),order="date_ asc", limit="1")
            all = updates | all 
            
        
       # master = updates.get.context()
        
        #for x in updates and y in transfers:
        #    product = x.context.get('product_id')
            
        
    
    