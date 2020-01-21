# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class masterinventory(models.Model):
    _name = 'zadara_inventory.master_inventory'
    _description = 'zadara_inventory.master_inventory'
    name = fields.Char()
    
    

    
    inv_product = fields.Many2one('zadara_inventory.product')
    
    inv_location = fields.Many2one('zadara_inventory.locations')                             
    
    inv_product_sn = fields.Many2one('zadara_inventory.serialnumbers')#compute="compute_sn")#compute="compute_sn", inverse="inv_compute_sn")
    
    inv_product_quant = fields.Many2one("zadara_inventory.quant")
    
    
    
   # @api.depends('inv_product')
   # def compute_sn(self):
   #     if self.inv_product.product_trackSerialNumber == False:
   #         self.inv_product_sn = 'N/A'
    
    #vals_list = {         'name': 'arbitrary',
                    #'inv_product': self.inv_product,
                    #'inv_location': self.inv_location, 
                    #'inv_product_sn': self.inv_product_sn,
                    # 'inv_product_quant': self.inv_product_quant}   
    @api.model_create_multi
    def create(self,vals_list):
     
            
        res = super(masterinventory, self).create(vals_list)
        return res
        #for vals in vals_list:
          #  if self.env.context.get('inv_product') and self.env.context.get('inv_location'):
           #     if self.env.context.get('inv_product_sn') and  self.env.context.get('inv_product_quant'):
           #         return 
        

            
           