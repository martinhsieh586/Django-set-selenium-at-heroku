web: gunicorn pyfin.wsgi --timeout 1200
     gunicorn --timeout 1200 view:finaly
celeryd: python manage.py celeryd -E -B --loglevel=INFO