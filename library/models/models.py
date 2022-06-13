# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Books'

    title = fields.Char()
    author = fields.Char()
    summary = fields.Text()
    published = fields.Date()
