{
    'name': 'Student Course Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students, courses, and enrollments',
    'description': """
        Student Course Management System
        =================================
        This module allows you to:
        * Manage students
        * Manage courses
        * Track student enrollments
        * Generate reports for student courses
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
        'views/menu_views.xml',
        'report/student_course_report.xml',
        'report/student_course_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
