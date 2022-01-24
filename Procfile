web: gunicorn pyfin.wsgi --timeout 1200
     gunicorn --timeout 1200 search:finaly.view
celeryd: python finaly.view celeryd -E -B --loglevel=INFO