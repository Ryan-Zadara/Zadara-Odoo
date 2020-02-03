# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class product(models.Model):
    _name = 'zadara_inventory.product'
    _description = 'zadara_inventory.product'
    
    name = fields.Char(default=lambda self: self.env.product_name)
    product_name = fields.Char()
    #product_id = fields.Char()
    part_number = fields.Char()
    product_category = fields.Char()
    
    mi_product = fields.One2many('zadara_inventory.master_inventory', 'product_id')
    
    
    total_quantity = fields.Integer()
    #product_grab = fields.Char() #must be product
    
    product_trackSerialNumber = fields.Boolean()
    
    location_id = fields.Many2one('zadara_inventory.locations')
    @api.onchange('product_name')
    def corr_name(self):
        self.name = self.product_name
    def get_track(self):
        return self.product_trackSerialNumber
    
    

    
    def action_(self):
        #t = self.env['zadara_inventory.product'].search[]
        vals_list = self.env['zadara_inventory.product'].search([])
        
        vals_list.compute_quantity()
     
        #raise UserError(self.id)
        action = {
            "type": "ir.actions.act_window",
            "view_mode": "tree,form,kanban",
            "res_model": 'zadara_inventory.product',
            }
        return action 
    
    def compute_quantity(self):
        #if self.location_id == None: 
        di = {}
        test = 0
        if not self.location_id:
            for x in self:
                test = test +1
                count = 0
                for y in x.mi_product:
                    if y.product_id.id == x.id:
                        count = count + y.quantity 
        else:
            for x in self:
                test = test +1
                count = 0
                for y in x.mi_product:
                    if y.product_id.id == x.id and y.location_id.id == x.location_id.id:
                        count = count + y.quantity 
           
               # i = i + t.quantity
                    vals_list = {'total_quantity' : count}
                    x.write(vals_list)
        #raise UserError(test)
        return 
    
    def write(self,vals_list):
        
        res = super(product, self).write(vals_list)
        return res
            
