# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Uno(models.Model):
    _name = 'uno.uno'
    _description = 'Dummy model'

    flag = fields.Boolean(string='Some random flag', default=True)
