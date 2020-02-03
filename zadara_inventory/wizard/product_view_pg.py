# -*- coding: utf-8 -*-

from odoo import fields, models, _
from datetime import datetime


class inv_report_calc(models.TransientModel):
    _name = 'zadara_inventory.inv_report_calc'
    _description = 'Stock Quantity History'
    
    location_id = fields.Many2one('zadara_inventory.locations')
    
    
    