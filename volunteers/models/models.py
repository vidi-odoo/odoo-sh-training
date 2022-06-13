# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'volunteers.task'
    _description = 'Voluteer Tasks'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    start_time = fields.Datetime(string='Start time')
    stop_time = fields.Datetime(string='Stop time')
    times_repeated = fields.Integer(string='Times repeated')
    frequency = fields.Selection(string='Frequency', selection=[
        ('hour', 'Hour'),
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year')
    ])