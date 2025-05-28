# Embassy of Mozambique Website

## Project Overview
This project aims to create a secure, modern, and fully functional website for the Embassy of Mozambique in France. The website will serve as the primary digital gateway for Mozambican citizens and French residents seeking consular services, information, and assistance.

## Technology Stack
- **Backend**: Django 4.2+
- **Frontend**: Bootstrap 5 or Tailwind CSS
- **Database**: PostgreSQL (production), SQLite (development)
- **Authentication**: Django's built-in authentication with OAuth2 integration
- **Deployment**: Docker containerization

## Features
- User Management & Authentication
- Appointment Booking System
- AI-Powered Chatbot
- Document Management System

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd embassy-mozambique-website
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - For development, use SQLite (default).
   - For production, configure PostgreSQL in `settings.py`.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the website at `http://127.0.0.1:8000/`.
- Use the admin panel to manage users and appointments.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. See the LICENSE file for details.