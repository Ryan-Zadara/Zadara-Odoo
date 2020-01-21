# -*- coding: utf-8 -*-


from odoo import models, fields, api


class moves(models.Model):
    _name = 'zadara_inventory.moves'
    _description = 'zadara_inventory.zadara_inventory'
    _inherit = 'zadara_inventory.move_line'
    name = fields.Char()
    
    move_type = fields.Char()
    
    
    #location_source = fields.Many2one('zadara_inventory.locations')
    #location_destination = fields.Many2one('zadara_inventory.locations')
    #transaction_id = fields.Char()
    
    #tracking_number = fields.Char()
    #products_moved = fields.Char()# Many2many('zadara_inventory.master_inventory')
  

    
class quantity_add(models.Model):
    _name = 'zadara_inventory.quantity_add'
    _description = 'zadara_inventory.zadara_inventory'
    
    name = fields.Char()
    
    mov_lin = fields.Many2many('zadara_inventory.move_line','inv_product', 'inv_location')
    
    move_line_id = fields.Many2one('zadara_inventory.move_line')
    
    
    inv_product = fields.Many2one(related='mov_lin.inv_product')
    
    inv_location = fields.Many2one(related='mov_lin.inv_location')  
                    
    inv_product_sn = fields.Many2one(related='move_line_id.inv_product_sn')
    
    inv_product_quant = fields.Many2one(related='move_line_id.inv_product_quant')
    
    vals_list = {
                    #'name': 'arbitrary',
                    #'inv_product': mov_lin.inv_product,
                    #'inv_location': mov_lin.inv_location, 
                    #'inv_product_sn': mov_lin.inv_product_sn,
                    #'inv_product_quant': mov_lin.inv_product_qunat,
                }
        
    
   # date = fields.Char()
  
    @api.model_create_multi
    def create(self,vals_list):
        #check if all things are correct
        vals_list = {
                    'name': 'arbitrary',
                    'inv_product': self.inv_product,
                    'inv_location': self.inv_location, 
                    'inv_product_sn': self.inv_product_sn,
                    'inv_product_quant': self.inv_product_quant,
                    'move_line_id': self.move_line_id

                }
        res = super(quantity_add, self).create(vals_list)
        self.send_qu()
        return res
    
    def send_qu(self):
        
        new_addtion = self.env['zadara_inventory.move_line'].create({
                  
                    'inv_product': self.inv_product,
                    'inv_location': self.inv_location, 
                    'inv_product_sn': self.inv_product_sn,
                     'inv_product_quant': self.inv_product_quant,
                })