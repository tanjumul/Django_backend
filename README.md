# Django Setup Commands

## Virtual Environment
```bash
# Create virtual environment
python3 -m venv <environment_name>

# Activate virtual environment (Linux/Mac)
source <environment_name>/bin/activate

# Activate virtual environment (Windows)
<environment_name>\Scripts\activate

# Deactivate virtual environment
deactivate

# Install Django
pip install django

# Create a new Django project
django-admin startproject <project_name>

# Run development server
python manage.py runserver

# Create a new app within project
python manage.py startapp <app_name>
