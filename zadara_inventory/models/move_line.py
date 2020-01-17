# -*- coding: utf-8 -*-


from odoo import models, fields, api


class move_line(models.Model):
    _name = 'zadara_inventory.move_line'
    _description = 'zadara_inventory.zadara_inventory'
    
    name = fields.Char()
    #location_source = fields.Many2one('zadara_inventory.locations')
    #location_destination = fields.Many2one('zadara_inventory.locations')
    transaction_id = fields.Char()
    
#    products_to_move = fields.Many2Many('zadara_inventory.master_inventory')

    
    