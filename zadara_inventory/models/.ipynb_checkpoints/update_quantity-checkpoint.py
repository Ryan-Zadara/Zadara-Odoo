# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class update_quantity(models.Model):
    _name = 'zadara_inventory.update_quantity'
    _description = 'zadara_inventory.upadate_quantity'

    #update_quantity_name = fields.Char(compute="comp_qn",store=True, default=lambda self: self.env['zadara_inventory.update_quantity'].comp_qn())
    
    location_id = fields.Many2one('zadara_inventory.locations')
    
    product_id = fields.Many2one('zadara_inventory.product')
    
    #product_trackSerialNumber = fields.Boolean(related="product_id.product_trackSerialNumber")
    
    product_name = fields.Char(related="product_id.product_name")
    
    serial_number = fields.Char()
    #p_tag = fields.Selection([('New','New'), ('Used','Used'),('Obsolete','Obsolete')], default='New')
    quantity = fields.Integer()
    product_number = fields.Many2one('zadara_inventory.product_number')
    
    responsible_party = fields.Selection([('Irvine','Irvine'), ('Yokneam','Yokneam')])
    
    update_date = fields.Datetime(default=lambda self: fields.datetime.now())
    #def date_set(self): 
     #   return datetime.now()datetime.strptime(Date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M')
    update_tag = fields.Char(readonly=True)
    p_tag = fields.Many2one('zadara_inventory.p_tag', string="Product Tag")

    t_quantity = fields.Integer(readonly=True)
    #moveline = fields.Many2many('zadara_inventory.mlqu')
    #@api.depends('update_date')
    #def comp_qn(self):
    #    if self.update_date == False:
            #self.date_set()
    #        raise UserError(self.update_date)
    #    r = self.update_date.to_string()
    #    return r
        #x = self.env['zadara_inventory.update_quantity'].search([],order="update_quantity_name desc", limit=1)
        #self.update_quantity_name = x.update_quantity_name
        #raise UserError(datetime.now()-)
        #if datetime.now() == self.update_date:
            
         #   r = x.update_quantity_name
        #self.update_quantity_name = r
        #else:
         #   r = x.update_quantity_name+1
        #return r
    #@api.onchange('product_id')
    #def fix_track(self):
    #    self.product_trackSerialNumber = self.product_id.product_trackSerialNumber
    #relation 
    #move = fields.Many2one('zadara_inventory.moves')
    
    #checks procdure valid, location_id, product_id 
    #precheck quatity not <0 
        #1 prpoduct tracking serial number or not 
            #2 if yes 
                #makes sure qunatity is 1, make sure sn is unique and not = to N/A or blank
            #2 if not 
                #make sn = too N/A, see if product exists at location 
                #if yes
                    #write over quantity 
                #if not 
                    #create instance with quantity at 
    def check_create_qu(self,q):
        if q > 1 or q < 0:
            raise UserError("bad")
    
    def pre_checks(self,q):
        if q < 0:
            raise UserError("quantitys cannot be negetive")
        
    
    @api.model_create_multi
    def create(self,vals_list):
        #datetime.strptime(Date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M')
       # uqn_val = self.comp_qn()
       # for x in vals_list:
         #   x['update_quantity_name'] = uqn_val
        for val in vals_list:
            
            val['t_quantity'] = val.get('quantity')
            if not val.get('product_id'):
                raise UserError("no product")
            if val.get('reponsible_party') == '':
                raise UserError("no responsible party")
            
            if not self.env['zadara_inventory.product_number'].search([['product_id.id','=',val.get("product_id")],['id','=',val.get('product_number')]]):
                raise UserError('product number not found')
            #if not val.get('update_date'):
            #    val['update_date'] = datetime.now()
           
            if 0 > val.get("quantity"):
                raise UserError('No quantities less than 0')
            track = self.env['zadara_inventory.product'].search([['id','=',val.get("product_id")],['product_trackSerialNumber','=',True]])
            if not val.get('location_id'):
                raise UserError("no location")
            if track:
                if val.get('quantity') < 0 or val.get('quantity') > 1:
                    raise UserError("bad quantity")
                if not val.get('serial_number'):
                    raise UserError('bad sn line')
                if val.get('serial_number') == 'N/A':
                    raise UserError('bad sns')                
                if self.env['zadara_inventory.master_inventory'].search([['serial_number', '=', val.get('serial_number')]]):
               #     if #self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['quantity','!=', val.get('quantity')]]):
                        #del val["product_trackSerialNumber"]
                        #del val["update_quantity_name"]
                   #     val['update_tag'] = 'write'
                 #   elif self.env['zadara_inventory.master_inventory'].search([['product_id', '=', val.get('product_id')], ['serial_number', '=', val.get('serial_number')],['quantity','=', val.get('quantity')]]):
                    raise UserError("cannot have 2 same serial numbers ")
                else:        
                    val['update_tag'] = 'create'
                #self.check_create_qu(q) 
            else:
                val['serial_number'] = "N/A"
                if self.env['zadara_inventory.master_inventory'].search([['location_id','=', val.get('location_id')],['product_id', '=',val.get('product_id')]]):
                    #del val["update_quantity_name"]
                    p = self.env['zadara_inventory.master_inventory'].search([['location_id','=', val.get('location_id')],['product_id', '=',val.get('product_id')]]).quantity
                    val['quantity'] = val.get('quantity') + p
                    val['update_tag'] = 'write'#self.write_to_mi(val)
                else:
                    val['update_tag'] = 'create'
                    
                    
             
                
          
        res = super(update_quantity, self).create(vals_list)
        for vals in vals_list:
            if vals.get('t_quantity'):
                del vals["t_quantity"]
            if vals.get('update_quantity_name'):
                del vals["update_quantity_name"]
            if vals.get('responsible_party'):
                del vals['responsible_party']
            #self.env['zadara_inventory.product_history'].create(vals)
            if vals.get('update_date'):
                del vals['update_date']
            if vals.get('update_tag') == 'create':
                del vals['update_tag']
                self.create_to_mi(vals)
            else:
                del vals['update_tag']
                self.write_to_mi(vals)
        
        return res
    
   
  
    @api.model
    def create_to_mi(self, vals_list):
        
        new_addition = self.env['zadara_inventory.master_inventory'].create(vals_list)
        if vals_list.get('product_number'):
            del vals_list['product_number']
        if vals_list.get('p_tag'):
            del vals_list['p_tag']
        self.env['zadara_inventory.product_history'].create(vals_list)

    def write_to_mi(self,vals_list):
        
        x = vals_list.get('product_id')
        
        sn = vals_list.get('serial_number')
        mi = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', x], ['serial_number', '=', sn],['location_id','=',vals_list.get('location_id')]])
        mi.write(vals_list)
        if vals_list.get('product_number'):
            del vals_list['product_number']
        if vals_list.get('p_tag'):
            del vals_list['p_tag']
        self.env['zadara_inventory.product_history'].create(vals_list)
        return 
    
    def write(self,vals_list):
        res = super(update_quantity, self).write(vals_list)
        return res
    
    
    
    
    # def sn_no_null(self):

        #for i in self:
        #    if i.product_id.sudo().product_trackSerialNumber == True:
        #        if serial_number == None:
        #            raise ValidationError("no sn")
                    
    #check product type 
   # @api.constrains('serial_number')
    #def check_sn(self):
     #   if self.env['zadara_inventory.master_inventory'].check_invforsn(t.product_id,t.serial_number):
      #      raise ValidationError("same sn")
                
    #check serial numbers 
    #create
    
    
    
    