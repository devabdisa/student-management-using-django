# Dil Fere School Portal

A comprehensive school management system built with Django, designed for primary schools to manage students, staff, attendance, results, timetables, and parent communication.

[![Django](https://img.shields.io/badge/Django-4.2.17-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)]()

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [User Roles](#user-roles)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Screenshots](#screenshots)
- [Demo Credentials](#demo-credentials)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 🎯 Overview

**Dil Fere School Portal** is a modern, full-featured school management system that streamlines administrative tasks, enhances communication between teachers and parents, and provides real-time insights into student performance.

### Key Highlights

- ✅ **5 User Roles** - Admin, Registrar, Staff, Student, Guardian
- ✅ **Modern UI** - Clean, professional SaaS-style interface
- ✅ **Timetable Management** - Complete scheduling system
- ✅ **Attendance Tracking** - Real-time attendance monitoring
- ✅ **Results Management** - Academic performance tracking
- ✅ **Parent Portal** - Guardian access to children's data
- ✅ **Mobile Responsive** - Works on desktop, tablet, and mobile
- ✅ **PostgreSQL Support** - Production-ready database support
- ✅ **Easy Setup** - Quick installation and configuration

---

## ✨ Features

### 👨‍💼 Admin/HOD Features

- **Dashboard Analytics** - Visual charts and statistics
- **User Management** - Manage staff, students, registrars, and guardians
- **Academic Management** - Courses, subjects, and sessions
- **Timetable Management** - Create and manage class schedules
- **Attendance Oversight** - View all attendance records
- **Results Oversight** - Monitor student performance
- **Leave Management** - Approve/reject leave applications
- **Feedback System** - Review and respond to feedback
- **Notifications** - Send announcements to all users

### 📋 Registrar Features

- **Read-Only Access** - View all student and staff records
- **Data Verification** - Verify attendance and results data
- **Reports** - Generate statistical reports
- **Timetable View** - Access class schedules
- **Dashboard** - System-wide statistics

### 👨‍🏫 Staff/Teacher Features

- **Attendance Management** - Take and update attendance
- **Results Entry** - Add and edit student results
- **Class Overview** - View assigned students and subjects
- **Leave Application** - Apply for time off
- **Feedback** - Communicate with administration
- **Timetable** - View teaching schedule

### 🎓 Student Features

- **Attendance View** - Check attendance records
- **Results View** - View academic performance
- **Timetable** - View class schedule
- **Leave Application** - Request absence
- **Feedback** - Send messages to administration
- **Profile Management** - Update personal information

### 👨‍👩‍👧 Parent/Guardian Features

- **Children Overview** - View all linked children
- **Attendance Monitoring** - Track children's attendance
- **Results Monitoring** - View children's academic performance
- **Timetable Access** - Check children's schedules
- **Notifications** - Receive school updates
- **Multi-Child Support** - Manage multiple children

### 🗓️ Timetable System

- **Time Slot Management** - Define class periods
- **Weekly Scheduling** - Monday to Friday schedules
- **Conflict Detection** - Prevent teacher double-booking
- **Room Assignment** - Assign classrooms
- **Role-Based Views** - Different views for each role

---

## 👥 User Roles

| Role | User Type | Access Level | Dashboard |
|------|-----------|--------------|-----------|
| **Admin/HOD** | 1 | Full system access | `/admin_home` |
| **Staff/Teacher** | 2 | Teaching features | `/staff_home` |
| **Student** | 3 | Student portal | `/student_home` |
| **Registrar** | 4 | Read-only data access | `/registrar_home` |
| **Parent/Guardian** | 5 | Children's data only | `/guardian_home` |

For detailed role permissions, see [USER_TYPES.md](USER_TYPES.md)

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 4.2.17 LTS
- **Language:** Python 3.12+
- **Database:** SQLite (default) / PostgreSQL (production)
- **ORM:** Django ORM

### Frontend
- **UI Framework:** Bootstrap 5
- **Admin Template:** AdminLTE (customized)
- **Custom CSS:** Modern design system
- **Charts:** Chart.js
- **Icons:** Font Awesome
- **Fonts:** Inter (Google Fonts)

### Additional Libraries
- **Pillow** - Image processing
- **WhiteNoise** - Static file serving
- **dj-database-url** - Database configuration
- **psycopg2-binary** - PostgreSQL adapter (optional)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git (for cloning)
- PostgreSQL (optional, for production)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-management-using-django.git
   cd student-management-using-django
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment**
   ```bash
   copy .env.example .env
   ```
   Edit `.env` and set your `SECRET_KEY` and other settings.

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser --email admin@dilfere.school
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000/`

For detailed setup instructions, see [SETUP.md](SETUP.md)

---

## 📚 Documentation

- **[USER_GUIDE.md](USER_GUIDE.md)** - Complete user guide for all roles
- **[SETUP.md](SETUP.md)** - Installation and configuration guide
- **[DEMO_CREDENTIALS.md](DEMO_CREDENTIALS.md)** - Test account credentials
- **[USER_TYPES.md](USER_TYPES.md)** - User role reference
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and changes

---

## 📸 Screenshots

### Admin Dashboard
![Admin Dashboard](ss/admin1.png)
*Modern admin dashboard with statistics and charts*

### Staff Dashboard
![Staff Dashboard](ss/staff1.png)
*Teacher dashboard with attendance and results management*

### Student Dashboard
![Student Dashboard](ss/student1.png)
*Student portal with attendance and results view*

### Manage Students
![Manage Students](ss/admin2.png)
*Student management interface*

### Manage Staff
![Manage Staff](ss/admin3.png)
*Staff management interface*

### Timetable View
![Timetable](ss/admin4.png)
*Weekly timetable management*

---

## 🔐 Demo Credentials

### Quick Test Accounts

**Admin Account:**
- Email: `admin@admin.com`
- Password: `admin`

**Registrar Account:**
- Email: `registrar@dilfere.school`
- Password: `registrar123`

**Guardian Account:**
- Email: `guardian@dilfere.school`
- Password: `guardian123`

For complete demo credentials and testing guide, see [DEMO_CREDENTIALS.md](DEMO_CREDENTIALS.md)

⚠️ **Security Note:** Change all default passwords before deploying to production!

---

## 🎨 UI/UX Features

### Modern Design System

- **Color Palette:** Professional indigo, green, amber, and red scheme
- **Typography:** Inter font family for clean readability
- **Components:** Modern stat cards, clean tables, rounded buttons
- **Responsive:** Mobile-friendly layout
- **Accessibility:** WCAG compliant color contrasts

### Dashboard Highlights

- **Stat Cards:** Large numbers with colored icon badges
- **Charts:** Interactive Chart.js visualizations
- **Tables:** Clean headers with hover effects
- **Forms:** Modern inputs with focus states
- **Notifications:** Real-time in-app notifications

---

## 🗄️ Database Support

### SQLite (Default)
- Perfect for development and testing
- No additional setup required
- Included with Python

### PostgreSQL (Recommended for Production)
- Scalable and robust
- Better performance for large datasets
- Full transaction support

See [SETUP.md](SETUP.md) for PostgreSQL configuration.

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Optional - PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Optional - Email (currently disabled)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

---

## 🧪 Testing

### Run System Check
```bash
python manage.py check
```

### Run Tests (if available)
```bash
python manage.py test
```

### Manual Testing
1. Login with each role
2. Test CRUD operations
3. Verify navigation
4. Check permissions
5. Test forms and validation

---

## 🚢 Deployment

### Preparation

1. **Set environment variables**
   ```env
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com
   DATABASE_URL=postgresql://...
   ```

2. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

### Deployment Options

- **Heroku** - See `Procfile` included
- **AWS** - EC2, RDS, S3
- **DigitalOcean** - Droplets, Managed Databases
- **PythonAnywhere** - Easy Django hosting
- **Docker** - Containerized deployment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add your feature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide
- Write clear commit messages
- Add tests for new features
- Update documentation
- Ensure all tests pass

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support

### Getting Help

- **Documentation:** Check the docs folder
- **Issues:** [GitHub Issues](https://github.com/yourusername/student-management-using-django/issues)
- **Email:** support@dilfere.school

### Reporting Bugs

When reporting bugs, please include:
- Python version
- Django version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/screenshots

---

## 🙏 Acknowledgments

- **Original Project:** [jobic10/student-management-using-django](https://github.com/jobic10/student-management-using-django)
- **UI Framework:** [AdminLTE](https://adminlte.io/)
- **Charts:** [Chart.js](https://www.chartjs.org/)
- **Icons:** [Font Awesome](https://fontawesome.com/)
- **Images:** [Unsplash](https://unsplash.com/)

---

## 🗺️ Roadmap

### Version 1.1 (Planned)
- [ ] Email notifications
- [ ] SMS notifications for guardians
- [ ] Advanced reporting (PDF/Excel export)
- [ ] Calendar view for events
- [ ] Bulk import/export

### Version 2.0 (Future)
- [ ] Mobile app (React Native)
- [ ] REST API
- [ ] Real-time notifications (WebSockets)
- [ ] Multi-language support
- [ ] Dark mode
- [ ] Advanced analytics dashboard

---

## 📊 Project Stats

- **Lines of Code:** ~15,000+
- **Models:** 15+
- **Views:** 100+
- **Templates:** 70+
- **User Roles:** 5
- **Features:** 50+

---

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐️

---

## 📞 Contact

**Project Maintainer:** [Your Name]  
**Email:** your.email@example.com  
**LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)  
**Twitter:** [@yourhandle](https://twitter.com/yourhandle)

---

## 📅 Project Timeline

- **Original Release:** 2020
- **Major Refactor:** May 2026
- **Current Version:** 1.0.0
- **Status:** Production Ready ✅

---

**Made with ❤️ for Dil Fere Primary School**

---

*Last Updated: May 8, 2026*
