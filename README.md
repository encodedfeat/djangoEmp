# Employee Management System

A Django-based web application for managing and displaying employee information with photo uploads and detailed profiles.

## 📋 Project Overview

This project is a simple yet effective Employee Management System built with Django. It allows you to manage employee records, including their contact information, position, photo, and description. Employees can be viewed in a list on the home page and clicked to view their detailed profile.

## ✨ Features

- **Employee Directory**: Browse all employees in a single list view
- **Employee Profiles**: View detailed information for individual employees
- **Photo Management**: Upload and display employee photos
- **Employee Information**: Store and display:
  - First and Last Name
  - Email Address
  - Phone Number
  - Position/Job Title
  - Description/Bio
  - Timestamps (Created & Updated dates)

## 🛠️ Tech Stack

- **Backend**: Django 6.0.6
- **Database**: SQLite
- **Image Processing**: Pillow 12.2.0
- **Environment Management**: python-dotenv 1.2.2
- **Database ORM**: SQLAlchemy (via sqlparse 0.5.5)
- **Python Version**: 3.x

## 📁 Project Structure

```
emp/
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── README.md                  # Project documentation
├── employees/                 # Main app for employee management
│   ├── models.py             # Employee data model
│   ├── views.py              # View logic
│   ├── urls.py               # URL routing for employees app
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── tests.py              # Unit tests
│   └── migrations/           # Database migrations
├── mysite/                   # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL configuration
│   ├── views.py              # Project-level views (home)
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── templates/                # HTML templates
│   ├── home.html            # Employee list page
│   └── employees.html       # Employee detail page
├── media/                   # User-uploaded files
│   └── images/             # Employee photos
├── static/                 # Static files
│   ├── css/
│   │   └── home.css       # Stylesheet
│   ├── images/            # Static images
│   └── js/                # JavaScript files
└── env/                    # Virtual environment
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd emp
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv env
   env\Scripts\activate
   
   # macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django==6.0.6 python-dotenv pillow sqlparse
   ```
   Or install from a requirements.txt file if available:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env file in the project root:**
   ```
   SECRET_KEY=your-secret-key-here
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Home Page: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## 📖 Usage

### Adding Employees

1. Go to the Admin Panel (`http://127.0.0.1:8000/admin/`)
2. Log in with your superuser credentials
3. Navigate to "Employees" section
4. Click "Add Employee" and fill in the required information:
   - First Name
   - Last Name
   - Email
   - Phone Number
   - Position
   - Description
   - Photo (upload an image)
5. Click "Save"

### Viewing Employees

- **Home Page**: Shows a list of all employees
- **Employee Detail**: Click on an employee to view their full profile with photo and details

## 🗄️ Models

### Employee_details

```python
class Employee_details(models.Model):
    first_name          # CharField (max 100 characters)
    last_name           # CharField (max 100 characters)
    photo               # ImageField (uploaded to 'images' folder)
    phone_number        # CharField (max 13 characters, optional)
    email               # CharField (max 100 characters)
    position            # CharField (max 100 characters)
    description         # CharField (max 500 characters)
    created_at          # DateTimeField (auto-generated on creation)
    updated_at          # DateTimeField (auto-updated on modification)
```

## 📌 URL Patterns

| URL | View | Purpose |
|-----|------|---------|
| `/` | `home` | Display all employees |
| `/employee/<id>/` | `Emp_details` | Display individual employee details |
| `/admin/` | Django Admin | Manage employees (admin only) |

## 🔧 Configuration

### Media Files
- Employee photos are uploaded to the `media/images/` directory
- Configure media settings in `mysite/settings.py`

### Static Files
- CSS, JavaScript, and static images are in the `static/` directory
- Run `python manage.py collectstatic` before deployment

## 🧪 Testing

Run tests using:
```bash
python manage.py test employees
```

## 📝 Future Enhancements

- Add employee search and filter functionality
- Implement employee editing and deletion features
- Add department management
- Create employee leave/attendance tracking
- Generate employee reports
- Add user authentication for employees
- Implement advanced admin features
- Add API endpoints for mobile app integration

## 🔐 Security Notes

- Never commit `.env` file to version control
- Keep `SECRET_KEY` secure in production
- Use environment variables for sensitive data
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` properly in production settings
- Use HTTPS in production

## 📦 Dependencies

- **django==6.0.6**: Web framework
- **python-dotenv==1.2.2**: Environment variable management
- **pillow==12.2.0**: Image processing
- **sqlparse==0.5.5**: SQL parsing
- **asgiref==3.11.1**: ASGI utilities
- **tzdata==2026.2**: Timezone data

## 📄 License

This project is provided as-is for educational and personal use.

## 🤝 Contributing

Feel free to fork this project, make improvements, and submit pull requests.

## 📧 Support

For issues or questions, please create an issue in the project repository.

---

**Created**: 2026
**Framework**: Django 6.0.6
**Database**: SQLite
