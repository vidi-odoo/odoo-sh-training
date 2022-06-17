# -*- coding: utf-8 -*-
# from odoo import http
from odoo.http import Controller, route, request

class MissionController(Controller):
    @route('/spacecrew', auth='public', website=True)
    def index(self):
        return 'Hello, space cadets!'
    
    @route('/spacecrew/missions', auth='public', website=True)
    def list(self):
        return request.render('spacecrew.mission_listing', {
            'missions': request.env['spacecrew.mission'].search([])
        })