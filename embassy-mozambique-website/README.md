# Embassy of Mozambique Website 🇲🇿

A comprehensive Django-based website for the Embassy of Mozambique in France, providing consular services, appointment booking, document management, and multilingual support.

## 🌟 Features

- **Multi-language Support**: English, Portuguese, and French
- **Appointment Booking System**: Online appointment scheduling for embassy services
- **Document Management**: Upload, review, and manage consular documents
- **CMS (Content Management System)**: Dynamic page and news management
- **User Authentication**: Custom user profiles with role-based access
- **Chatbot Integration**: AI-powered assistance for common queries
- **Responsive Design**: Mobile-friendly Bootstrap-based interface
- **Admin Dashboard**: Comprehensive administration panel

## 🏗️ Project Structure

```
embassy-mozambique-website/
├── src/
│   ├── embassy_website/          # Main project configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── accounts/             # User management & authentication
│   │   ├── appointments/         # Appointment booking system
│   │   ├── services/             # Embassy services catalog
│   │   ├── cms/                  # Content management system
│   │   ├── documents/            # Document management
│   │   └── chatbot/              # AI chatbot functionality
│   ├── templates/                # HTML templates
│   │   ├── base.html
│   │   ├── cms/
│   │   ├── accounts/
│   │   └── ...
│   ├── static/                   # Static files (CSS, JS, images)
│   │   └── css/
│   │       └── main.css
│   └── media/                    # User uploaded files
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd embassy-mozambique-website
```

2. **Create and activate virtual environment**
```bash
# Create virtual environment
python -m venv embassy_env

# Activate virtual environment
# On macOS/Linux:
source embassy_env/bin/activate
# On Windows:
embassy_env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Navigate to project directory**
```bash
cd src
```

5. **Create database and run migrations**
```bash
# Create migrations
python manage.py makemigrations accounts
python manage.py makemigrations services
python manage.py makemigrations cms
python manage.py makemigrations appointments
python manage.py makemigrations documents
python manage.py makemigrations chatbot

# Apply migrations
python manage.py migrate
```

6. **Create superuser account**
```bash
python manage.py createsuperuser
```

7. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

8. **Run the development server**
```bash
python manage.py runserver
```

9. **Access the website**
- Main website: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## 📦 Dependencies

### Core Dependencies
- **Django 4.2+**: Web framework
- **django-allauth**: Authentication and social login
- **djangorestframework**: API development
- **django-cors-headers**: CORS handling
- **django-crispy-forms**: Form styling
- **crispy-bootstrap5**: Bootstrap 5 integration
- **Pillow**: Image processing
- **python-dotenv**: Environment variables
- **whitenoise**: Static file serving

### Optional Dependencies
- **openai**: ChatGPT integration for chatbot
- **celery**: Asynchronous task processing
- **redis**: Caching and message broker

## 🛠️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optional - defaults to SQLite)
DATABASE_URL=postgresql://user:password@localhost:5432/embassy_db

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=embassy@mozambique.fr

# OpenAI API (for chatbot)
OPENAI_API_KEY=your-openai-api-key
```

### Django Settings

Key settings in `settings.py`:

- **AUTH_USER_MODEL**: Custom user model
- **LANGUAGE_CODE**: Default language (English)
- **TIME_ZONE**: Europe/Paris
- **STATIC_URL**: Static files configuration
- **MEDIA_URL**: Media files configuration

## 🎨 Customization

### Styling

The project uses Bootstrap 5 with custom CSS incorporating Mozambican flag colors:

```css
:root {
    --moz-green: #009639;
    --moz-red: #DC143C;
    --moz-yellow: #FFD700;
    --moz-black: #000000;
}
```

### Templates

Templates are organized by app:
- `templates/base.html`: Main layout template
- `templates/cms/home.html`: Homepage template
- `templates/accounts/`: Authentication templates
- `templates/appointments/`: Booking templates

## 🔧 Development

### Running Tests

```bash
python manage.py test
```

### Code Quality

```bash
# Check for issues
python manage.py check

# Check deployment readiness
python manage.py check --deploy
```

### Database Management

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (development only)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📊 Admin Interface

The Django admin interface provides comprehensive management for:

- **Users & Permissions**: User accounts, roles, and permissions
- **Services**: Embassy services catalog
- **Appointments**: Booking management and scheduling
- **Documents**: Document types, templates, and user uploads
- **CMS**: Pages, news articles, and content blocks
- **Chatbot**: Knowledge base and chat sessions

## 🌐 Multilingual Support

The website supports three languages:

1. **English** (default)
2. **Portuguese** (Mozambican official language)
3. **French** (Host country language)

### Adding Translations

```bash
# Generate translation files
python manage.py makemessages -l pt
python manage.py makemessages -l fr

# Compile translations
python manage.py compilemessages
```

## 🚀 Deployment

### Production Checklist

1. Set `DEBUG = False`
2. Configure proper `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Set up proper database (PostgreSQL recommended)
5. Configure email backend
6. Set up static file serving
7. Configure HTTPS
8. Set up logging

### Environment Setup

```bash
# Production settings
export DEBUG=False
export ALLOWED_HOSTS=your-domain.com
export DATABASE_URL=your-production-database-url
```

## 🤖 Chatbot Integration

The project includes an AI-powered chatbot for user assistance:

- Knowledge base management
- Multi-language support
- Session tracking
- Integration with OpenAI GPT models

## 📱 API Endpoints

The project includes REST API endpoints for:

- User authentication
- Appointment management
- Document handling
- Service information

Access API documentation at: `/api/docs/`

## 🔒 Security Features

- CSRF protection
- XSS protection
- SQL injection prevention
- Secure password handling
- Rate limiting
- Input validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Support

For support and questions:

- **Email**: support@mozambique-embassy.fr
- **Phone**: +33 (0) 1 XX XX XX XX
- **Address**: Embassy of Mozambique, Paris, France

## 🔄 Version History

- **v1.0.0** (2025-01-01): Initial release
  - Basic CMS functionality
  - User authentication
  - Appointment booking system
  - Document management
  - Multilingual support

## 🛣️ Roadmap

### Upcoming Features

- [ ] Payment integration for visa fees
- [ ] SMS notifications
- [ ] Calendar integration
- [ ] Advanced reporting
- [ ] Mobile app API
- [ ] Advanced chatbot features
- [ ] Integration with government systems

---

**Embassy of Mozambique in France** 🇲🇿  
*Serving the Mozambican community with excellence*