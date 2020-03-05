# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class p_tag(models.Model):
    _name = 'zadara_inventory.p_tag'
    _description = 'p_tag'


    name = fields.Char(compute="p_tag_makename",store=True)
    #('BrokenNoWarranty','BrokenNoWarranty')
    p_tag_type = fields.Selection([('New','New'), ('Used','Used'),('Obsolete','Obsolete'),('RMA','RMA'),('Broken No Warranty','Broken No Warranty')])

    p_tag_desc = fields.Char(string="RMA Number")

    @api.depends('p_tag_type','p_tag_desc')
    def p_tag_makename(self):
        if not self.p_tag_desc == False:
            self.name = str(self.p_tag_type)+' '+ str(self.p_tag_desc)
        else:
            self.name = str(self.p_tag_type)

    @api.model_create_multi
    def create(self,vals_list):
        for x in vals_list:
            if x.get('p_tag_type') == 'RMA' and x.get('p_tag_desc') == False:
                raise UserError("If product tag type is RMA the RMA number must be included")
            #for t in 
            if self.env['zadara_inventory.p_tag'].search([['name','=',x.get('name')]]):
                raise UserError("Product Tag already made")
        res = super(p_tag, self).create(vals_list)
        return res 