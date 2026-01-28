# Installation and Quick Start Guide

## Prerequisites

- Odoo 14.0 or later installed and running
- Access to Odoo addons directory
- Admin rights in Odoo

## Installation

### Step 1: Deploy the Module

```bash
# Navigate to your Odoo addons directory
cd /path/to/odoo/addons

# Copy or clone the student_course module
cp -r /path/to/student-repo/student_course .
```

### Step 2: Update Odoo Apps List

**Option A: Restart Odoo**
```bash
# Restart your Odoo service
sudo systemctl restart odoo
# or
sudo service odoo restart
```

**Option B: Update from UI**
1. Log in to Odoo as Administrator
2. Enable Developer Mode (Settings → Activate the developer mode)
3. Go to Apps menu
4. Click "Update Apps List"
5. Click "Update" in the confirmation dialog

### Step 3: Install the Module

1. Go to **Apps** menu
2. Remove the "Apps" filter to see all modules
3. Search for "Student Course Management"
4. Click **Install** button

## Quick Start

### 1. Create Your First Course

1. Go to **Student Management → Courses**
2. Click **Create**
3. Fill in the details:
   - **Name**: Introduction to Python
   - **Code**: CS101
   - **Credits**: 3
   - **Instructor**: Dr. Smith
   - **Description**: Basic Python programming course
4. Click **Save**

### 2. Add a Student

1. Go to **Student Management → Students**
2. Click **Create**
3. Fill in the details:
   - **Name**: John Doe
   - **Student ID**: STU001
   - **Email**: john.doe@example.com
   - **Phone**: +1234567890
4. Click **Save**

### 3. Create an Enrollment

1. Go to **Student Management → Enrollments**
2. Click **Create**
3. Select:
   - **Student**: John Doe
   - **Course**: Introduction to Python
   - **Enrollment Date**: (today's date is default)
   - **Status**: Enrolled
4. Click **Save**

### 4. Generate Your First Report

1. Stay on the enrollment record you just created
2. Click the **Print** button at the top
3. Select **Student Course Report**
4. The PDF report will be generated and downloaded automatically

## Sample Data

You can add this sample data to test the module:

### Courses
- **CS101** - Introduction to Python (3 credits)
- **CS102** - Data Structures (4 credits)
- **MATH201** - Calculus I (4 credits)
- **ENG101** - English Composition (3 credits)

### Students
- **STU001** - John Doe (john.doe@example.com)
- **STU002** - Jane Smith (jane.smith@example.com)
- **STU003** - Bob Johnson (bob.j@example.com)

### Create multiple enrollments to test reports

## Verification

To verify the installation:

1. ✅ Check that "Student Management" menu appears in the main menu bar
2. ✅ Verify you can access Students, Courses, and Enrollments submenus
3. ✅ Create a test student and course
4. ✅ Create a test enrollment
5. ✅ Generate a report from the enrollment

## Troubleshooting

### Module Not Appearing in Apps List
- Make sure the module is in the correct addons directory
- Update the apps list (Apps → Update Apps List)
- Check Odoo logs for errors

### Permission Errors
- Ensure you're logged in as Administrator
- Check that security/ir.model.access.csv is properly loaded

### Report Not Generating
- Check that wkhtmltopdf is installed (required for PDF reports)
- Verify report templates are properly loaded
- Check Odoo logs for template errors

### Installation Failed
- Check dependencies (base module should be available)
- Verify all XML files are valid
- Check Odoo logs for specific errors

## Next Steps

After installation:

1. **Customize Fields**: Add more fields to models based on your needs
2. **Setup Users**: Create user accounts with appropriate permissions
3. **Import Data**: Use Odoo's import feature to bulk load students/courses
4. **Configure Settings**: Adjust module settings as needed
5. **Train Users**: Provide training on how to use the system

## Support

For issues or questions:
- Check the README.md for detailed documentation
- Review TECHNICAL.md for architecture details
- Check Odoo community forums
- Review Odoo documentation at https://www.odoo.com/documentation

## Uninstallation

To uninstall the module:

1. Go to **Apps** menu
2. Search for "Student Course Management"
3. Click **Uninstall**
4. Confirm the uninstallation

**Note**: Uninstalling will remove all data (students, courses, enrollments). Back up your data before uninstalling.
