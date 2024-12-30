from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    deadline_date = fields.DateTime(string='Deadline Date', required=False)
    budget = fields.Float(string='Budget', required=False)
    project_size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large')
    ], string='Project Size', required=False)