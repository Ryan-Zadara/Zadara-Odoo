# -*- coding: utf-8 -*-

from odoo import models, fields, api


class masterinventory(models.Model):
    _name = 'zadara_inventory.master_inventory'
            
    _description = 'zadara_inventory.master_inventory'

    name = fields.Char()
    
    product_ids = fields.Many2one('zadara_inventory.product')#, domain="[('product_grab', '=', 'product')])
    product_location = fields.Many2one('zadara_inventory.locations')                             
    
    product_sn = fields.Char(compute="compute_sn", inverse="inv_compute_sn")
    tracksn = fields.Boolean(related="product_ids.product_trackSerialNumber", store=True)
    #quant = fields.Integer()
    
    
    @api.depends('product_ids','tracksn')
    def compute_sn(self):
       
        if not self.tracksn: 
            self.product_sn = 'N/A'
      #  else:
       #     self.update(self.product_sn) 
    @api.depends('product_ids','tracksn')
    def inv_compute_sn(self):
       product_sn = fields.Char()
        
    
    
    