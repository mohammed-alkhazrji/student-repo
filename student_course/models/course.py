from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'student.course.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    description = fields.Text(string='Description')
    credits = fields.Integer(string='Credits')
    instructor = fields.Char(string='Instructor')
    enrollment_ids = fields.One2many('student.course.enrollment', 'course_id', string='Enrollments')
    enrollment_count = fields.Integer(string='Enrollment Count', compute='_compute_enrollment_count', store=False)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Course code must be unique!')
    ]

    @api.depends('enrollment_ids')
    def _compute_enrollment_count(self):
        for record in self:
            record.enrollment_count = len(record.enrollment_ids)

    @api.constrains('credits')
    def _check_credits(self):
        for record in self:
            if record.credits and record.credits <= 0:
                raise ValidationError('Credits must be positive')
