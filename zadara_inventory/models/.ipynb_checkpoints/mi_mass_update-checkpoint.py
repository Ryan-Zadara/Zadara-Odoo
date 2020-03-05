# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError , UserError

class mi_mass_update(models.Model):
    _name = 'zadara_inventory.mi_mass_update'
    _description = 'zadara_inventory.mi_mass_update'
    
   
    
    serial_number = fields.Char()
    
    location_id = fields.Many2one('zadara_inventory.locations')                             
    
    quantity = fields.Integer()
    product_number = fields.Many2one('zadara_inventory.product_number')
    #p_tag = fields.Selection([('New','New'), ('Used','Used'),('Obsolete','Obsolete')])
    p_tag = fields.Many2one('zadara_inventory.p_tag', string="Product Tag")

    
    @api.model_create_multi
    def create(self,vals_list):
        for x in vals_list:
            if not x.get('serial_number'):
                raise UserError('no SN')
            #if not x.get('location_id'):
            #   del x['location_id']
            #if not x.get('product_number'):
            #    del x['product_number']
            #if not x.get('quantity'):
            #    del x['quantity']
            #if not x.get('p_tag'):
            #    del x['p_tag']
      
        for x in vals_list:
            mi = self.env['zadara_inventory.master_inventory'].search([['serial_number','=',x.get('serial_number')]])
            #if len(mi) > 1:
              #  raise UserError("WARNING multiple products withthe same SN found")
           
            mi.write(x)  
        res = super(mi_mass_update, self).create(vals_list)
        return res
             #raise UserError("breatk")
        #if x.get('')