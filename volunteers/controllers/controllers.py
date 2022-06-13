# -*- coding: utf-8 -*-
# from odoo import http


# class Volunteers(http.Controller):
#     @http.route('/volunteers/volunteers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/volunteers/volunteers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('volunteers.listing', {
#             'root': '/volunteers/volunteers',
#             'objects': http.request.env['volunteers.volunteers'].search([]),
#         })

#     @http.route('/volunteers/volunteers/objects/<model("volunteers.volunteers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('volunteers.object', {
#             'object': obj
#         })
