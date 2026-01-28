from odoo import models, fields, api


class Enrollment(models.Model):
    _name = 'student.course.enrollment'
    _description = 'Student Course Enrollment'
    _rec_name = 'display_name'

    student_id = fields.Many2one('student.course.student', string='Student', required=True, ondelete='cascade')
    course_id = fields.Many2one('student.course.course', string='Course', required=True, ondelete='cascade')
    enrollment_date = fields.Date(string='Enrollment Date', default=fields.Date.today, required=True)
    grade = fields.Char(string='Grade')
    status = fields.Selection([
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped')
    ], string='Status', default='enrolled', required=True)
    display_name = fields.Char(string='Display Name', compute='_compute_display_name')

    @api.depends('student_id', 'course_id')
    def _compute_display_name(self):
        for record in self:
            if record.student_id and record.course_id:
                record.display_name = f"{record.student_id.name} - {record.course_id.name}"
            else:
                record.display_name = "New Enrollment"
