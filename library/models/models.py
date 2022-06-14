# -*- coding: utf-8 -*-
# pyright: basic

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Books'
    _rec_name = 'title'

    title = fields.Char('Title')
    author = fields.Char('Author')
    summary = fields.Text('Summary')
    publisher = fields.Char('Publisher')
    published = fields.Date('Published')
    isbn = fields.Char('ISBN')
    notes = fields.Text('Notes')
    genre = fields.Char('Genre')

