Maykin Media Test

Requirements:
Install Python 3.8 or newer and make sure to select to install pip as well - https://www.python.org/downloads/

You will need to type **pip install packagename** in the command prompt for the following
If this does not work try **python -m pip install packagename**

django --> https://www.djangoproject.com/
django-crispy-forms --> https://django-crispy-forms.readthedocs.io/en/latest/ (Used for making the forms a bit cleaner)
requests --> https://pypi.org/project/requests/ (Used for importing the data over HTTP)
django-crontab --> https://pypi.org/project/django-crontab/ (PLEASE NOTE THIS DOES NOT WORK ON WINDOWS. This is only used for an example of how a cronjob could be used and is not actually implemented. If you don't want to install this then you will need to comment out 'django_crontab', in the installed apps in settings.py)

Type the command - "python manage.py import_data" to import the data from the csv files into the database. You may want to run "python manage.py flush" and then "yes" before doing so in order to empty the current database.
Type the command - "python manage.py runserver" and then go to http://127.0.0.1:8000/home to view the project
Type the command - "python manage.py help" for more commands
