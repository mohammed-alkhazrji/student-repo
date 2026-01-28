# Report Preview - Student Course Report

## What the Report Shows

When a user generates a "Student Course Report" from an enrollment record, they get a professional PDF document with the following structure:

---

### Report Layout

```
╔════════════════════════════════════════════════════════════════╗
║                     [Company Header/Logo]                       ║
╠════════════════════════════════════════════════════════════════╣
║                                                                 ║
║               Student Course Enrollment Report                  ║
║                                                                 ║
║───────────────────────────────────────────────────────────────║
║                                                                 ║
║  Student Information                                           ║
║  ┌──────────────────────────────────────────────────────────┐ ║
║  │ Student Name:    John Doe                                 │ ║
║  │ Student ID:      STU001                                   │ ║
║  │ Email:           john.doe@example.com                     │ ║
║  │ Phone:           +1234567890                              │ ║
║  └──────────────────────────────────────────────────────────┘ ║
║                                                                 ║
║  Course Information                                            ║
║  ┌──────────────────────────────────────────────────────────┐ ║
║  │ Course Name:     Introduction to Python                   │ ║
║  │ Course Code:     CS101                                    │ ║
║  │ Credits:         3                                        │ ║
║  │ Instructor:      Dr. Smith                                │ ║
║  │ Description:     Basic Python programming course          │ ║
║  └──────────────────────────────────────────────────────────┘ ║
║                                                                 ║
║  Enrollment Details                                            ║
║  ┌──────────────────────────────────────────────────────────┐ ║
║  │ Enrollment Date: 2024-01-15                               │ ║
║  │ Status:          Enrolled                                 │ ║
║  │ Grade:           A                                        │ ║
║  └──────────────────────────────────────────────────────────┘ ║
║                                                                 ║
╠════════════════════════════════════════════════════════════════╣
║                     [Company Footer]                            ║
║                     Page 1 of 1                                ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Report Features

### ✅ Professional Formatting
- Clean, organized layout with clear sections
- Bootstrap-based styling for consistent appearance
- Proper spacing and typography
- Table-based layout for easy reading

### ✅ Comprehensive Information
**Student Section:**
- Complete student profile
- Contact information
- Unique student identifier

**Course Section:**
- Full course details
- Credit hours
- Instructor name
- Course description

**Enrollment Section:**
- When the student enrolled
- Current enrollment status
- Academic grade (if assigned)

### ✅ Standard Odoo Layout
- Uses Odoo's `web.external_layout`
- Includes company header/logo (if configured)
- Professional footer with page numbers
- Consistent with other Odoo reports

### ✅ PDF Output
- High-quality PDF generation
- Printable format
- Ready for archiving or sharing
- Can be emailed directly from Odoo

---

## How to Access the Report

### From Enrollment List View:
1. Navigate to: **Student Management → Enrollments**
2. Select one or more enrollment records (checkbox)
3. Click **Print** button in the action bar
4. Choose **Student Course Report**
5. PDF downloads automatically

### From Enrollment Form View:
1. Open any enrollment record (double-click from list)
2. Click **Print** button (top toolbar)
3. Select **Student Course Report**
4. PDF generated instantly

### Bulk Printing:
- Select multiple enrollments in list view
- Generate reports for all selected records
- Each enrollment gets its own page in the PDF
- Single download contains all reports

---

## Use Cases

### For Students:
- Enrollment verification
- Record keeping
- Registration confirmation
- Academic documentation

### For Administration:
- Enrollment verification
- Course roster documentation
- Academic records
- Transfer documentation

### For Faculty:
- Class roster information
- Student contact details
- Enrollment confirmations
- Grade documentation

---

## Technical Details

**Report Type:** QWeb PDF  
**Model:** student.course.enrollment  
**Template:** report_student_course_document  
**Binding:** Enrollment records  
**Format:** PDF (A4/Letter)  
**Multi-record:** Yes (supports bulk printing)  

**Dependencies:**
- wkhtmltopdf (for PDF conversion)
- Odoo web module (for layouts)
- Bootstrap CSS (for styling)

---

## Customization Options

The report can be easily customized by editing the template:

### Add More Fields:
- Student photo
- Course prerequisites
- Academic year/semester
- Tuition fee information
- Attendance statistics

### Modify Layout:
- Change colors/styling
- Add company logo/watermark
- Include additional sections
- Modify table formatting

### Add Calculations:
- GPA display
- Credit totals
- Cost calculations
- Progress indicators

### Branding:
- Custom headers/footers
- Color scheme matching
- Institution logo
- Official stamps/signatures

---

## Sample Report Scenarios

### Scenario 1: Active Enrollment
```
Student: Alice Johnson (STU002)
Course: Database Systems (CS202)
Status: Enrolled
Grade: [In Progress]
```

### Scenario 2: Completed Course
```
Student: Bob Wilson (STU003)
Course: Web Development (CS301)
Status: Completed
Grade: B+
```

### Scenario 3: Dropped Course
```
Student: Carol Davis (STU004)
Course: Advanced Math (MATH301)
Status: Dropped
Grade: [Not Applicable]
```

---

## Report Quality Assurance

✅ **Tested Features:**
- Single record printing
- Multiple record printing
- All data fields display correctly
- PDF formatting is consistent
- Layout is responsive
- Tables align properly

✅ **Validation:**
- Empty fields handled gracefully
- Long text wraps correctly
- Special characters display properly
- Date formatting is correct
- Status colors are clear

---

This report provides a professional, comprehensive document for student course enrollments that can be used for official purposes, record keeping, and verification.
