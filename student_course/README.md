# Student Course Management Addon for Odoo

This Odoo addon provides a complete student course management system with reporting capabilities.

## Features

### 1. Student Management
- Create and manage student records
- Track student information (name, ID, email, phone, date of birth, address)
- View all enrollments for each student

### 2. Course Management
- Create and manage course records
- Track course information (name, code, description, credits, instructor)
- View all enrollments for each course

### 3. Enrollment Management
- Link students to courses
- Track enrollment dates
- Manage enrollment status (Enrolled, Completed, Dropped)
- Record grades

### 4. Reporting
- **Student Course Report**: Generate PDF reports for student enrollments
  - Displays complete student information
  - Displays complete course information
  - Shows enrollment details including date, status, and grade
  - Professional formatted PDF output

## Installation

1. Copy the `student_course` folder to your Odoo addons directory
2. Update the addons list in Odoo
3. Install the "Student Course Management" module

## Usage

### Managing Students
1. Navigate to **Student Management → Students**
2. Click **Create** to add a new student
3. Fill in the student information
4. View enrollments in the Enrollments tab

### Managing Courses
1. Navigate to **Student Management → Courses**
2. Click **Create** to add a new course
3. Fill in the course information
4. View enrollments in the Enrollments tab

### Creating Enrollments
1. Navigate to **Student Management → Enrollments**
2. Click **Create** to add a new enrollment
3. Select a student and course
4. Set the enrollment date and status
5. Optionally add a grade

### Generating Reports
1. Navigate to **Student Management → Enrollments**
2. Select one or more enrollment records
3. Click **Print → Student Course Report**
4. The PDF report will be generated and downloaded

Alternatively:
1. Open an enrollment record
2. Click **Print → Student Course Report**
3. The PDF report will be generated for that specific enrollment

## Module Structure

```
student_course/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── student.py          # Student model
│   ├── course.py           # Course model
│   └── enrollment.py       # Enrollment model
├── views/
│   ├── student_views.xml   # Student views
│   ├── course_views.xml    # Course views
│   ├── enrollment_views.xml # Enrollment views
│   └── menu_views.xml      # Menu structure
├── report/
│   ├── student_course_report.xml    # Report action
│   └── student_course_template.xml  # Report template
└── security/
    └── ir.model.access.csv  # Access rights
```

## Technical Details

### Models

**student.course.student**
- Student information and profile
- One2many relationship with enrollments

**student.course.course**
- Course information and details
- One2many relationship with enrollments

**student.course.enrollment**
- Links students to courses
- Tracks enrollment status and grades
- Many2one relationships with student and course

### Reports

The module includes a QWeb PDF report that can be generated from enrollment records. The report includes:
- Student details
- Course information
- Enrollment information (date, status, grade)

## Dependencies

- base (Odoo core module)

## License

This module is provided as-is for educational purposes.
