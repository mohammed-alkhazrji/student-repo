from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.course.student'
    _description = 'Student'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    date_of_birth = fields.Date(string='Date of Birth')
    address = fields.Text(string='Address')
    enrollment_ids = fields.One2many('student.course.enrollment', 'student_id', string='Enrollments')
    enrollment_count = fields.Integer(string='Enrollment Count', compute='_compute_enrollment_count')

    @api.depends('enrollment_ids')
    def _compute_enrollment_count(self):
        for record in self:
            record.enrollment_count = len(record.enrollment_ids)
