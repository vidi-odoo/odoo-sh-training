# pyright: basic

from odoo import models, fields, api


class ProjectWizard(models.TransientModel):
    _name = 'spacecrew.project.wizard'

    def _default_mission(self):
        return self.env['spacecrew.mission'].browse(self.env.context.get('active_id'))

    mission_id = fields.Many2one('spacecrew.mission', 'Mission',
                                 required=True,
                                 default=_default_mission)
    # Related fields
    name = fields.Char('Name', related='mission_id.name')
    start_date = fields.Datetime('Start Date', related='mission_id.launch_date')
    end_date = fields.Datetime('End Date', related='mission_id.return_date')
    
    # User-customizable fields
    summary = fields.Html('Summary')

    def create_project(self):
        self.env['project.project'].create({
            'name': f'{self.name} Project',
            'date_start': self.start_date,
            'date_end': self.end_date,
            'mission_id': self.mission_id.id,
            'description': self.summary
        })
