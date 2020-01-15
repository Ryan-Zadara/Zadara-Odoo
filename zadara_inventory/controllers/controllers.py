# -*- coding: utf-8 -*-
from odoo import http


class ZadaraInventory(http.Controller):
    @http.route('/zadara_inventory/zadara_inventory/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/zadara_inventory/zadara_inventory/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('zadara_inventory.listing', {
            'root': '/zadara_inventory/zadara_inventory',
            'objects': http.request.env['zadara_inventory.zadara_inventory'].search([]),
        })

    @http.route('/zadara_inventory/zadara_inventory/objects/<model("zadara_inventory.zadara_inventory"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('zadara_inventory.object', {
            'object': obj
        })
