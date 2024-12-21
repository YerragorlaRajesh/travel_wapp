python manage.py collectstatic --noinput
gunicorn travel_wapp.wsgi:application --bind=0.0.0.0:8000
