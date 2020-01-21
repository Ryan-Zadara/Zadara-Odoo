#-*- coding: utf-8 -*-

from odoo import models, fields, api


class zadara_inventory(models.Model):
    _name = 'zadara_inventory.zadara_inventory'
    _description = 'zadara_inventory.zadara_inventory'

    name = fields.Char()
    value = fields.Integer()
 

            
class test_(models.Model):
        _name = 'zadara_inventory.test_'
       # _inherit = 'zadara_inventory.zadara_inventory'
        m = fields.Many2many('zadara_inventory.zadara_inventory')