release: python manage.py migrate
web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn blog.wsgi
