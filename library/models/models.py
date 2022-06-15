# -*- coding: utf-8 -*-
# pyright: basic

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    rental_id = fields.Many2one('library.rental', 'Rental')

    @api.onchange('isbn')
    def _onchange_isbn(self):
        if self.isbn and len(self.isbn) != 13:
            raise ValidationError(
                f'ISBN {self.isbn} is not valid: needs to be 13 characters long'
            )

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Rentals'

    name = fields.Char('Name', related='customer_id.name')
    customer_id = fields.Many2one('res.partner', 'Customer', required=True)
    book_ids = fields.One2many('library.book', 'rental_id', 'Books', readonly=True)