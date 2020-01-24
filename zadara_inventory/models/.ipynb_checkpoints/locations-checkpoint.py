# -*- coding: utf-8 -*-

from odoo import models, fields, api


class locations(models.Model):
    _name = 'zadara_inventory.locations'
    _description = 'locations'

    name = fields.Char()
    address = fields.Char()
    location_type = fields.Char()
    #location_id = fields.Char(readonly="true")