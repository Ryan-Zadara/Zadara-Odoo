# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_history(models.Model):
    _name = 'zadara_inventory.product_history'
    _description = 'zadara_inventory'
    
    product_id = fields.Many2one('zadara_inventory.master_inventory')
    
    location_id  = fields.Many2one('zadara_inventory.locations', readonly=True)
    
    date_ = fields.Datetime()
    @api.model
    def create(self,vals_list):
        if vals_list.get('update_date'):
            vals_list['date_'] = vals_list.get('update_date')
            del vals_list['update_date']
        if vals_list.get('transfer_date'):
            vals_list['date_'] = vals_list.get('transfer_date')
            del vals_list['transfer_date']
        if vals_list.get('quantity'):
            del vals_list['quantity']
        if vals_list.get('serial_number'):
            del vals_list['serial_number']
        if vals_list.get('transfer_tag'):
            
            del vals_list["transfer_tag"]
        if vals_list.get('update_tag'):
            del vals_list['update_tag']
        res = super(product_history, self).create(vals_list)
        return res
        
        