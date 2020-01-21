# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError


class move_line(models.Model):
    _name = 'zadara_inventory.move_line'
    

    inv_product = fields.Many2one('zadara_inventory.product')
    
    inv_location = fields.Many2one('zadara_inventory.locations')    
                    
    inv_product_sn = fields.Many2one('zadara_inventory.serialnumbers')
    
    inv_product_quant = fields.Many2one('zadara_inventory.quant')
      
    #product_ids = inv_product.ids   
   
    #@api.onchange("inv_product")
    #def constrain_product(self):
        
    #@api.constrains('inv_product_sn')
    #def contstrain_sn(self):
    #    if self.env['zadara_inventory.serialnumbers'].check_sns(self.inv_product_sn):
     #        raise ValidationError("cannot have a repeat sn")
    
    @api.constrains('inv_product_sn')
    def constrains_sn_inv(self):
        for x in self:
            if x.env['zadara_inventory.master_inventory'].check_invforsn(x.inv_product_sn, x.inv_product):
                raise ValidationError("must have unique serial number for"%self.inv_product_sn )
  
            
    vals_list = {'inv_product': '',
                 'inv_location': '' ,
                    'inv_product_sn': '',
                'inv_product_quant': '' }
    
   #@api.depends('inv_product')
    #def update_p_vals_list(self):
    #    vals_list.update({'inv_product', self.inv_product})
        
   # @api.depends('serialnumbers')
   # def update_sn_vals_list(self):
   #     vals_list.update({'serialnumbers', self.serialnumbers})

    @api.model_create_multi
    def create(self, vals_list):      
        res = super(move_line, self).create(vals_list)
        new_addtion = res.env['zadara_inventory.move_line'].send_to_mi(vals_list)
        return res

    def send_to_mi(self,vals_list):
        #if self.inv_product != None and self.inv_location != None:
         #   if self.inv_product_sn != None and self.inv_product_quant != None: 
        #name = fields.Char()
       # temp_dic = dict('name' ,"arbitrary")
       # vals_list.append({'name' : "arbitrary"})
        #if tag_aux == True:
       # vals_list = {'name': 'arbitrary', 
        #                  'inv_product': selfinv_product,
         #           'inv_location': self.inv_location, 
          #          'inv_product_sn': self.inv_product_sn,
           #          'inv_product_quant': self.inv_product_quant,}
        
        new_addtion = self.env['zadara_inventory.master_inventory'].create(vals_list)
                   # 'name': 'arbitrary',
                   #'inv_product': self.inv_product,
                   # 'inv_location': self.inv_location, 
                    #'inv_product_sn': self.inv_product_sn,
                     #'inv_product_quant': self.inv_product_quant,
                #})
            