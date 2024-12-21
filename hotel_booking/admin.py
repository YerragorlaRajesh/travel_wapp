from django.contrib import admin
from .models import Hotel, Booking

# Register the Hotel model
admin.site.register(Hotel)

# Register the Booking model
admin.site.register(Booking)
