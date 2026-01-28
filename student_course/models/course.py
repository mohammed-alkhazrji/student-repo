from odoo import models, fields, api


class Course(models.Model):
    _name = 'student.course.course'
    _description = 'Course'
    _rec_name = 'name'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    description = fields.Text(string='Description')
    credits = fields.Integer(string='Credits')
    instructor = fields.Char(string='Instructor')
    enrollment_ids = fields.One2many('student.course.enrollment', 'course_id', string='Enrollments')
    enrollment_count = fields.Integer(string='Enrollment Count', compute='_compute_enrollment_count')

    @api.depends('enrollment_ids')
    def _compute_enrollment_count(self):
        for record in self:
            record.enrollment_count = len(record.enrollment_ids)
