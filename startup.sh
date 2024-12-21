#!/bin/bash
python manage.py shell << EOF
from travel_wapp.utils import get_rajesh_user
get_rajesh_user()
print("Rajesh user setup completed")
EOF


# Start Gunicorn
gunicorn travel_wapp.wsgi:application --bind=0.0.0.0:8000