# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError , UserError

class master_inventory(models.Model):
    _name = 'zadara_inventory.master_inventory'
    _description = 'zadara_inventory.master_inventory'
   # name = fields.Char()
    
    
   

    p_tag = fields.Many2one('zadara_inventory.p_tag', string="Product Tag")

    product_id = fields.Many2one('zadara_inventory.product')

    #product_name = fields.Char(compute="set_name",store=True)

    

    
    location_id = fields.Many2one('zadara_inventory.locations')                             
    
    serial_number = fields.Char()
    #inv_product_sn = fields.Many2one('zadara_inventory.serialnumbers')#compute="compute_sn")#compute="compute_sn", inverse="inv_compute_sn")
    
    quantity = fields.Integer()
    
   # p_tag = fields.Selection([('New','New'), ('Used','Used'),('Obsolete','Obsolete')])
    #product_ids = inv_product.ids
    product_number = fields.Many2one('zadara_inventory.product_number')
 
    report_q_mi = fields.Integer(string="Total Quantity of item in Master Inventory", help="this field is only for reporting")
    
   
    #@api.depends('product_id')
   # def set_name(self):
     #   self.product_name = self.product_id.name

    #def check_invforsn(self,pid,sn):
     #   for i in self:
    #        if i.product_id == pid:
      #          if i.serial_number == sn:
       #             return True
        #        raise ValidationError(pid) 
        
    #def get_tot_qunant(self,product_):
        #q = self.env['zadara_inventory.product'].search([''])
       # for x in 
        #    raise UserError(x)
        
        #    i = i + x.quantity
      #  return 1
    @api.model
    def create(self,vals_list):
  
        res = super(master_inventory, self).create(vals_list)
        
        #self.env['zadara_inventory.product_history'].create(vals_list)
        
        #f = self.env['zadara_inventory.product']
        
        #f.compute_quantity(vals_list.get('product_id'))
        return res
    
    def get_recordset(self, pids):
        rset = self.env.ref(pids,['zadara_inventory.master_inventory'])
        return rset                 
    
    def return_tq(self,p_id):
        tot = 0
        for x in self: 
            if x.product_id.id == p_id:
                #raise UserError(p_id)         
                tot = tot + x.quantity 
        return tot
    
    def return_tq_wl(self,p_id,l_id):
        tot = 0
        
        for x in self: 
            #raise UserError(l_id)   
            if x.product_id.id == p_id and x.location_id.id == l_id:
                    
                tot = tot + x.quantity 
                
        return tot
                         
    def write(self,vals_list):
        x = self
        #raise UserError(vals_list.get('location_id'))
        res = super(master_inventory, self).write(vals_list)
        
       # if self.env['zadara_inventory.product'].search([['id','=',vals_list.get("product_id")],['product_trackSerialNumber','=',True]]):
        #    self.write({'location_id.id': vals_list.get('location_id')})

        #x.env['zadara_inventory.product_history'].create(vals_list)
       # self.env['zadara_inventory.product'].search(['id','=',vals_list.get('product_id')]).compute_quantity()
       # raise UserError(self.location_id.id)

        return res
        
        
   
        