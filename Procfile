web: gunicorn pyfin.wsgi --keep-alive 1200
     gunicorn finaly.view --keep-alive 1200
celeryd: python manage.py celeryd -E -B --loglevel=INFO