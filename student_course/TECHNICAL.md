# Student Course Addon - Technical Overview

## Architecture

### Data Model

```
┌─────────────────────┐
│   Student           │
│  (student.course.   │
│      student)       │
├─────────────────────┤
│ - name              │
│ - student_id        │
│ - email             │
│ - phone             │
│ - date_of_birth     │
│ - address           │
│ - enrollment_ids    │
└──────────┬──────────┘
           │
           │ One2Many
           │
           ▼
┌─────────────────────┐
│   Enrollment        │
│  (student.course.   │
│    enrollment)      │
├─────────────────────┤
│ - student_id        │
│ - course_id         │
│ - enrollment_date   │
│ - status            │
│ - grade             │
└──────────┬──────────┘
           │
           │ Many2One
           │
           ▼
┌─────────────────────┐
│   Course            │
│  (student.course.   │
│      course)        │
├─────────────────────┤
│ - name              │
│ - code              │
│ - description       │
│ - credits           │
│ - instructor        │
│ - enrollment_ids    │
└─────────────────────┘
```

### Menu Structure

```
Student Management (Root Menu)
├── Students
│   └── Tree and Form views
├── Courses
│   └── Tree and Form views
├── Enrollments
│   └── Tree and Form views
└── Reports
    └── Student Course Report
```

## Report Functionality

The **Student Course Report** is the core feature of this addon. It provides:

### Report Features
1. **Professional PDF Output**: Clean, formatted PDF reports
2. **Complete Information Display**:
   - Student details (name, ID, email, phone)
   - Course details (name, code, credits, instructor, description)
   - Enrollment information (date, status, grade)

### How to Generate Reports

#### Method 1: From Enrollment List
1. Go to **Student Management → Enrollments**
2. Select one or more enrollment records
3. Click **Print** button (or Action menu)
4. Select **Student Course Report**
5. PDF will be generated and downloaded

#### Method 2: From Single Enrollment
1. Open any enrollment record
2. Click **Print** button
3. Select **Student Course Report**
4. PDF will be generated for that enrollment

### Report Template Details

The report uses QWeb templating engine with:
- **Layout**: Standard Odoo external layout with header/footer
- **Styling**: Bootstrap CSS classes for professional appearance
- **Sections**:
  - Report header with title
  - Student information table
  - Course information table
  - Enrollment details table

### Report Configuration

The report is defined in two XML files:

1. **student_course_report.xml**: Defines the report action
   - Model: `student.course.enrollment`
   - Type: QWeb PDF
   - Binding: Available on enrollment records

2. **student_course_template.xml**: Defines the report layout
   - Template ID: `report_student_course_document`
   - Uses QWeb syntax for dynamic content
   - Loops through selected records

## File Structure

```
student_course/
├── __init__.py                          # Module initialization
├── __manifest__.py                      # Module manifest/configuration
├── README.md                            # User documentation
├── models/
│   ├── __init__.py                     # Models initialization
│   ├── student.py                      # Student model definition
│   ├── course.py                       # Course model definition
│   └── enrollment.py                   # Enrollment model definition
├── views/
│   ├── student_views.xml               # Student UI views
│   ├── course_views.xml                # Course UI views
│   ├── enrollment_views.xml            # Enrollment UI views
│   └── menu_views.xml                  # Menu structure
├── report/
│   ├── student_course_report.xml       # Report action definition
│   └── student_course_template.xml     # Report QWeb template
└── security/
    └── ir.model.access.csv             # Access rights configuration
```

## Key Features

### 1. Computed Fields
- `enrollment_count` on Student and Course models
- Automatically counts related enrollments
- Updates in real-time

### 2. Relational Integrity
- Many2One relationships with cascade delete
- Ensures data consistency
- Prevents orphaned records

### 3. Status Management
- Enrollment status: Enrolled, Completed, Dropped
- Helps track student progress
- Filterable in list views

### 4. Flexible Reporting
- Print single or multiple enrollment reports
- Consistent formatting
- Professional appearance

## Installation Steps

1. **Copy Module**: Place `student_course` folder in Odoo addons directory
2. **Update Apps List**: Restart Odoo or update apps list
3. **Install Module**: 
   - Go to Apps menu
   - Search for "Student Course Management"
   - Click Install

## Usage Workflow

### Typical Usage Flow:
1. **Setup Courses**: Create courses with details
2. **Add Students**: Register students with their information
3. **Create Enrollments**: Link students to courses
4. **Track Progress**: Update status and grades
5. **Generate Reports**: Print enrollment reports as needed

## Customization Points

The addon can be extended by:
- Adding more fields to models
- Creating additional reports (e.g., transcript, class roster)
- Adding computed fields (e.g., GPA calculation)
- Implementing workflows for enrollment approval
- Adding email notifications
- Creating dashboard views with statistics

## Dependencies

- **base**: Odoo core module (automatically available)

## Compatibility

- Designed for Odoo 14+ (compatible with 15, 16, 17)
- Uses standard Odoo ORM and QWeb
- No external dependencies required
