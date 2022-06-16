# pyright: basic

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    mission_id = fields.Many2one('spacecrew.mission', 'Mission')