# -*- coding: utf-8 -*-


from odoo import models, fields, api


class moves(models.Model):
    _name = 'zadara_inventory.moves'
    _description = 'zadara_inventory.zadara_inventory'
    
    name = fields.Char()
    location_source = fields.Many2one('zadara_inventory.locations')
    location_destination = fields.Many2one('zadara_inventory.locations')
    transaction_id = fields.Char()
    
    tracking_number = fields.Char()
    products_moved = fields.Many2many('zadara_inventory.master_inventory')

    
    
    
    
    
#class complete_move_button(models.Model):
#    _name = 'zadara_inventory.complete_move_button'