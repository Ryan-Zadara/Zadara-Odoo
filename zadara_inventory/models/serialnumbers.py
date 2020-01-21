# -*- coding: utf-8 -*-


from odoo import models, fields, api


class serialnumbers(models.Model):
    _name = 'zadara_inventory.serialnumbers'
    _description = 'zadara_inventory.zadara_inventory'
    
    
    product_ = fields.Many2one("zadara_inventory.product")
    
    #product_id = product_.id
    inventory_ = fields.Many2one("zadara_inventory.masterinventory")
    #inveotory_id = inventory_.id
    
    serialnumber = fields.Char()
    
    def check_sns(self, sn):
        for x in self:
            if x.serialnumber == sn:
                return True
        return False
    
    def check_invforsn(self,sn,producttype):
        
        for x in self.filtered(lambda r: r.product_ == producttype):
            if x.serialnumber == sn:
                return True 
        return False
        
    
    
    
    