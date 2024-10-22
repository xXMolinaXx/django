- settings.py el valor DIRS guarda la ruta a los templates
### Iniciar servidor
- python manage.py runserver
#### otros
- python manage.py startapp <nombre> para crear aplicacion
- las aplicaciones son sub divisiones del proyecto principal
- python -m django --version
- python manage.py runserver 8080 or python manage.py runserver 0.0.0.0:8000
- The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
- The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name. At this point, it’s worth reviewing what these arguments are for.
    - (kwargs) Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren’t going to use this feature of Django in the tutorial.
    - (name) Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.
### BD con django
1) python manage check 
2) python manage.py migrate (crear la base de datos y las tablas)
    - The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app
3) python manage.py makemigrations (crear la base de datos y las tablas)
    - By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
4) python manage.py sqlmigrate <nombre> <numero de migracion> ()
### abrir shell en mi entorno virtual
- python manage.py shell abrir un shel desde el proyecto

### DJANGO ADMIN
-  python manage.py createsuperuser
- /admin default url for admin

