# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class locations(models.Model):
    _name = 'zadara_inventory.locations'
    _description = 'locations'

    name = fields.Char()
    address = fields.Char()
    location_type = fields.Selection([('Warehouse','Warehouse'), ('Customer','Customer'),('Vendor','Vendor'),('Lab','Lab')])
    #location_id = fields.Char(readonly="true")
    @api.model_create_multi
    def create(self,vals_list):
        for y in vals_list:
            for x in self.env['zadara_inventory.locations'].search([]):
                if x.name == y.get('name'):
                    raise UserError("Location Already on file")
        res = super(locations, self).create(vals_list)
        return res