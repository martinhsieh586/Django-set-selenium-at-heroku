web: gunicorn pyfin.wsgi --timeout 1200
     gunicorn --timeout 1200 search:finaly
celeryd: python view.py celeryd -E -B --loglevel=INFO