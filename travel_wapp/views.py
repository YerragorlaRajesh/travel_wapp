from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.conf import settings

def home(request):
    try:
        # Try to get the Rajesh user
        rajesh_user = User.objects.get(username='Rajesh')
        print("Rajesh user already exists")
    except User.DoesNotExist:
        try:
            # Create Rajesh user if doesn't exist
            User.objects.create_superuser(
                username='Rajesh',
                password=settings.RAJESH_PASSWORD
            )
            print("Rajesh user created successfully!")
        except IntegrityError:
            print("Error creating user - might be a race condition")
    return render(request, 'home.html')