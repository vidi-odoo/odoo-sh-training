# -*- coding: utf-8 -*-
# pyright: basic

from odoo import models, fields, api


class Task(models.Model):
    _name = 'volunteers.task'
    _description = 'Voluteer Tasks'

    name = fields.Char('Name')
    description = fields.Text('Description')
    start_time = fields.Datetime('Start time')
    stop_time = fields.Datetime('Stop time')
    times_repeated = fields.Integer('Times repeated')
    frequency = fields.Selection([
        ('hour', 'Hour'),
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year')
    ], 'Frequency')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ready', 'Ready')
    ], 'State', default='draft')
    leader = fields.Char('Leader')
    volunteer_ids = fields.Many2many('res.partner', string='Volunteers')

    @api.onchange('leader')
    def _onchange_leader(self):
        if self.leader:
            self.state = 'ready'
