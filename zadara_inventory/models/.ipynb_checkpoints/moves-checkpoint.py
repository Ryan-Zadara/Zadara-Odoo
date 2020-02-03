# -*- coding: utf-8 -*-


from odoo import models, fields, api


class moves(models.Model):
    _name = 'zadara_inventory.moves'
    _description = 'zadara_inventory.zadara_inventory'
   
    
    uq_move_id = fields.Many2one('zadara_inventory.update_quantity')
    
    move_date = fields.Char()
    
    #update_quantity_name = fields.Char(related='uq_move_id.update_quantity_name')
    