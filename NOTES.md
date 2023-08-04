# Django Project

Django is a web framework writtern in Python.

When Django is installed, you can use `django-admin startproject spaghetti .`. This command will create a spaghetti subdirectory containing Django files. It will also create a manage.py file, which can be executed to interact with the Django project. For example, `python manage.py run-webserver` will start the webserver.

 Django has many built-in apps, including:
* admin interface to manage data
* ORM for SQL databases
* authentication for users
* caching data

The built-in apps are configured from settings.py inside the main Django project (in this case, spaghetti). To add custom features to Django, we can use the command `python manage.py startapp <feature-name>`. The name of the feature must then be added to settings.py under `INSTALLED_APPS`.
