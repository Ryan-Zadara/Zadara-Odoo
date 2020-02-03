# -*- coding: utf-8 -*-

from odoo import models, fields, api


class locations(models.Model):
    _name = 'zadara_inventory.locations'
    _description = 'locations'

    name = fields.Char()
    address = fields.Char()
    location_type = fields.Selection([('Warehouse','Warehouse'), ('Customer','Customer'),('Vendor','Vendor')])
    #location_id = fields.Char(readonly="true")