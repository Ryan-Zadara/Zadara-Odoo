# -*- coding: utf-8 -*-


from odoo import models, fields, api




class quant(models.Model):
    _name = 'zadara_inventory.qunat'
    _description = 'zadara_inventory.zadara_inventory'
    
    product_ = fields.Many2one("zadara_inventory.product")
    
    #product_id = product_.id
    
    quant = fields.Integer()
    
   
    
    
    #tracksn = fields.Boolean(related="product_ids.product_trackSerialNumber", store=True)
    
    #@api.constrains('product_sn','product_ids')
    #def check_sn(self):
        
    #    for x in self.env['mast_inv'].search(['pro_ids', '=','product_ids']):
    #        if product_sn == x.product_sn:
    #            raise ValidationError("2same sns")
                