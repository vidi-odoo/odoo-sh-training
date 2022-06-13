# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    _name = 'spacecrew.spaceship'
    _description = 'Spaceship'

    name = fields.Char()
    active = fields.Boolean(string='Active', default=True)
    manufacturer = fields.Char()