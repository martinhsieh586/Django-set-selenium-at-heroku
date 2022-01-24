web: gunicorn pyfin.wsgi --graceful-timeout 1200
     gunicorn --graceful-timeout 1200 search:finaly.view
celeryd: python finaly.view celeryd -E -B --loglevel=INFO