from django.contrib.auth.models import User

def get_rajesh_user():
    return User.objects.get(username='Rajesh')