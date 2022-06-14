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
    frequency = fields.Selection('Frequency', selection=[
        ('hour', 'Hour'),
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year')
    ])
