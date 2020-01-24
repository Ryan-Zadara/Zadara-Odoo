# -*- coding: utf-8 -*-


from odoo import models, fields, api


class move_line(models.Model):
    _name = 'zadara_inventory.move_line'
    _description = 'zadara_inventory.move_line'
   
    product 
    
    move_type = fields.Char()
    
    
    
    
    
    
    
    
    
    