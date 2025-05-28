# Navigate to your project directory first
cd /Users/linoospaulinos/python_project_2025/testweb/embassy-mozambique-website/src

# Make the manage.py file executable (if needed)
chmod +x manage.py

# Run Django commands using manage.py
python manage.py runserver

# Or if you made it executable, you can run it directly
./manage.py runserver

# Other common Django management commands:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py shell
python manage.py test

# Run on specific host and port
python manage.py runserver 0.0.0.0:8000

# Run with specific settings file
python manage.py runserver --settings=embassy_website.settings.production