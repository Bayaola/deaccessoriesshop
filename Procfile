release: python manage.py makemagrations
release: python manage.py migrate
web: gunicorn src.wsgi --log-file -