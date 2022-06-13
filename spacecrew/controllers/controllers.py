# -*- coding: utf-8 -*-
# from odoo import http


# class Spacecrew(http.Controller):
#     @http.route('/spacecrew/spacecrew', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spacecrew/spacecrew/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('spacecrew.listing', {
#             'root': '/spacecrew/spacecrew',
#             'objects': http.request.env['spacecrew.spacecrew'].search([]),
#         })

#     @http.route('/spacecrew/spacecrew/objects/<model("spacecrew.spacecrew"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spacecrew.object', {
#             'object': obj
#         })
