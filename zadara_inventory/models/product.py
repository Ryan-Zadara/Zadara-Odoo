# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class product(models.Model):
    _name = 'zadara_inventory.product'
    _description = 'zadara_inventory.product'
    
    name = fields.Char(compute='corr_name',store=True)
    product_name = fields.Char(required=True)
    #product_id = fields.Char()
    part_number = fields.One2many('zadara_inventory.product_number', 'product_id')

    product_category = fields.Selection([('Drive','Drive'), ('Cable','Cable'), ('Transceiver','Transceiver'),('Tray','Tray'),('Server','Server'),('Switch','Switch'),('Firewall','Firewall'),('Card','Card'),('CPU','CPU'),('Router','Router'),('Adapter','Adapter')])

    
    mi_product = fields.One2many('zadara_inventory.master_inventory', 'product_id')
    
    locat_loc_id = fields.Char()
    
    vendor_id = fields.Many2one('zadara_inventory.vendors')
    
    total_quantity = fields.Integer()
    #product_grab = fields.Char() #must be product
    
    product_trackSerialNumber = fields.Boolean(string="Product Track By Serial Number:")
    
    location_id = fields.Many2one('zadara_inventory.locations')
    @api.depends('product_name','name','vendor_id','product_category')
    def corr_name(self):
        self.name = str(self.product_category) + ' ' + str(self.vendor_id.short_name) + ' ' + str(self.product_name)
       #self.name = self.product_name
    def get_track(self):
        return self.product_trackSerialNumber
    
    
    
   # def set_o(self,p_id):
       # x = self.env['zadara_inventory.master_inventory'].search('product_id','=',p_id)
    
            
    
    def action_(self):
        #t = self.env['zadara_inventory.product'].search[]
        #vals_list = self.env['zadara_inventory.product'].search([])
        #x = self.env['zadara_inventory.product'].search([])
        #vals_list.compute_quantity()
        self.compute_quantity()
        #raise UserError(self.id)
        action = {
            "type": "ir.actions.act_window",
            "name": "Products",
            "view_mode": "tree,form,kanban",
            "res_model": 'zadara_inventory.product',
            }
        return action 
    
    def compute_quantity(self):
        for x in self:
            x.locat_loc_id = ''
            unt = self.env['zadara_inventory.master_inventory'].search([])
            count = unt.return_tq(x.id)
            #raise UserError(unt)
            x.total_quantity = count
        
        #for x in self.env['zadara_inventory.master_inventory'].search([]):
            
            
          #  unt = self.env['zadara_inventory.master_inventory'].return_tq(x.id)
           # count = unt
           # raise UserError(count)
           # vals_list = {'total_quantity' : count}
           # self.write(vals_list)
            
        #for x in self.env['zadara_inventory.master_inventory'].search([]):
           
           # nq = nq + x.quantity
        #vals_list = [{'total_quantity':nq}]
        #raise UserError("hi")
       # self.env['zadara_inventory.product'].write(vals_list)
        #if self.location_id == None: 
       # di = {}
        #test = 0
        #if not self.location_id:
        #    for x in self:
        #        test = test +1
        #        count = 0
        #        for y in x.mi_product:
        #            if y.product_id.id == x.id:
        #                count = count + y.quantity 
        #else:
        #    for x in self:
        #        test = test +1
        #        count = 0
        #        for y in x.mi_product:
        #            if y.product_id.id == x.id and y.location_id.id == x.location_id.id:
        #                count = count + y.quantity 
           
               # i = i + t.quantity
         #           vals_list = {'total_quantity' : count}
         #           x.write(vals_list)
        
         
    
    def write(self,vals_list):
        
        res = super(product, self).write(vals_list)
       
        return res
            
