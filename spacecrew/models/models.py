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
    mission_ids = fields.One2many(
        'spacecrew.mission', 'spaceship_id', 'Missions'
    )

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


class Mission(models.Model):
    _name = 'spacecrew.mission'
    _description = 'Spacecrew Missions'

    spaceship_id = fields.Many2one(
        'spacecrew.spaceship', 'Spaceship', required=True
    )
    name = fields.Char('Name', related='spaceship_id.name')
    crew_ids = fields.Many2many('res.partner', string='Crew')
    launch_date = fields.Datetime('Launch Date')
    return_date = fields.Datetime('Return Date')

    fuel_required = fields.Float('Fuel Required',
                                 compute='_compute_fuel_required',
                                 help='Amount of fuel (in liters)',
                                 store=True)

    engines = fields.Integer('Engines',
                             required=True,
                             default=1)

    @api.depends('launch_date', 'return_date', 'engines')
    def _compute_fuel_required(self):
        for record in self:
            if record.launch_date and record.return_date:
                diff = record.return_date - record.launch_date
                record.fuel_required = diff.days * 650 * record.engines

    @api.constrains('launch_date', 'return_date')
    def _check_return_after_launch_date(self):
        for record in self:
            if record.return_date and record.launch_date and record.return_date < record.launch_date:
                raise UserError(
                    f"""
                    Invalid launch/return date: return date must be equal to or later than launch date
                    (launch date: {record.launch_date}, return date: {record.return_date})
                    """
                )
