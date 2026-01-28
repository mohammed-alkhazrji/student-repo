# Student Repository - Odoo Addons

This repository contains Odoo addons for educational management.

## Modules

### 📚 Student Course Management (`student_course`)

A complete student course management system with professional PDF reporting capabilities.

**Key Features:**
- 👤 **Student Management**: Comprehensive student profiles with contact information and enrollment tracking
- 📖 **Course Management**: Course catalog with details, credits, and instructor information
- 📝 **Enrollment Tracking**: Link students to courses with status tracking and grade management
- 📄 **PDF Report Generation**: Professional student course enrollment reports (⭐ Primary Feature)

**What's Included:**
- Three interconnected data models (Student, Course, Enrollment)
- Intuitive user interface with form and list views
- Menu-driven navigation
- Data validation and security
- Comprehensive documentation

See the [student_course README](student_course/README.md) for detailed documentation.

## 📋 Documentation

### For Users:
- **[User Guide](student_course/README.md)** - Features, usage, and how-to guides
- **[Installation Guide](student_course/INSTALL.md)** - Step-by-step installation with quick start
- **[Report Preview](student_course/REPORT_PREVIEW.md)** - Visual guide to report output

### For Developers:
- **[Technical Documentation](student_course/TECHNICAL.md)** - Architecture and implementation details
- **[Project Summary](student_course/SUMMARY.md)** - Complete overview of deliverables

## 🚀 Quick Start

### Installation

```bash
# Clone the repository to your Odoo addons directory
cd /path/to/odoo/addons
git clone <repository-url> student-repo

# Restart Odoo
sudo systemctl restart odoo

# In Odoo:
# 1. Go to Apps → Update Apps List
# 2. Search for "Student Course Management"
# 3. Click Install
```

### First Steps

1. **Create Courses**: Go to Student Management → Courses → Create
2. **Add Students**: Go to Student Management → Students → Create
3. **Enroll Students**: Go to Student Management → Enrollments → Create
4. **Generate Reports**: Select an enrollment → Print → Student Course Report

## 📊 Report Feature

The **Student Course Report** is the core feature of this addon:

- **Professional PDF Output**: Clean, formatted reports with Bootstrap styling
- **Comprehensive Information**: Student details, course info, and enrollment data
- **Easy Access**: One-click generation from enrollment records
- **Bulk Support**: Generate multiple reports at once
- **Standard Layout**: Uses Odoo's standard external layout with headers/footers

See [REPORT_PREVIEW.md](student_course/REPORT_PREVIEW.md) for visual examples.

## 🔒 Security

- ✅ CodeQL security scan passed (0 vulnerabilities)
- ✅ Data validation on all models
- ✅ Unique constraints prevent duplicate records
- ✅ Access control configured

## 🛠️ Technical Details

- **Odoo Version**: 14.0+ (compatible with 15, 16, 17)
- **Language**: Python 3, XML, QWeb
- **Database**: PostgreSQL (via Odoo ORM)
- **Dependencies**: base (Odoo core)
- **License**: Educational/Open Source

## 📁 Repository Structure

```
student-repo/
├── README.md                              # This file
├── .gitignore                            # Git ignore patterns
└── student_course/                       # Main addon
    ├── README.md                         # User documentation
    ├── INSTALL.md                        # Installation guide
    ├── TECHNICAL.md                      # Technical docs
    ├── SUMMARY.md                        # Project summary
    ├── REPORT_PREVIEW.md                 # Report examples
    ├── __manifest__.py                   # Addon manifest
    ├── models/                           # Data models
    │   ├── student.py                   # Student model
    │   ├── course.py                    # Course model
    │   └── enrollment.py                # Enrollment model
    ├── views/                           # UI views
    │   ├── student_views.xml
    │   ├── course_views.xml
    │   ├── enrollment_views.xml
    │   └── menu_views.xml
    ├── report/                          # Report templates
    │   ├── student_course_report.xml    # Report action
    │   └── student_course_template.xml  # QWeb template
    └── security/                        # Access rights
        └── ir.model.access.csv
```

## 🎯 Use Cases

### For Educational Institutions:
- Student information management
- Course catalog management
- Enrollment tracking
- Academic documentation
- Official enrollment certificates

### For Training Centers:
- Participant registration
- Course scheduling
- Completion tracking
- Certificate generation

### For Online Platforms:
- User course enrollment
- Progress tracking
- Achievement documentation

## 🔧 Customization

The addon can be extended with:
- Additional fields and attributes
- Custom report templates
- GPA calculation
- Attendance tracking
- Payment integration
- Email notifications
- Student portal
- Analytics dashboards

## 🤝 Contributing

This is an educational project. Feel free to:
- Report issues
- Suggest improvements
- Submit enhancements
- Create custom versions

## 📞 Support

For questions or issues:
1. Check the documentation in the `student_course` folder
2. Review the installation guide
3. Consult Odoo documentation at https://www.odoo.com/documentation

## ✅ Project Status

**Status**: ✅ Complete and Production Ready

All features implemented, tested, and documented. Ready for deployment in Odoo 14+ environments.

---

**Version**: 1.0  
**Last Updated**: 2026-01-28  
**Tested on**: Odoo 14.0+ 
