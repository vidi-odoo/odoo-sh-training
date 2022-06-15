# -*- coding: utf-8 -*-
# pyright: basic

from odoo import models, fields, api
from odoo.exceptions import UserError

class Spaceship(models.Model):
    _name = 'spacecrew.spaceship'
    _description = 'Spaceship'

    name = fields.Char('Name')
    active = fields.Boolean('Active', default=True)
    manufacturer = fields.Char('Manufacturer')
    width = fields.Float('Width', default=0.)
    height = fields.Float('Height', default=0.)

    @api.constrains('width', 'height')
    def _check_width_larger_than_height(self):
        for record in self:
            if record.width > record.height:
                raise UserError(
                    f"""
                    Invalid spaceship "{record.name}":
                    Width cannot be greater than height (width={record.width} > height={record.height})
                    """
                )
