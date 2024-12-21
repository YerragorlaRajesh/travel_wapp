from django.contrib import admin
from .models import Event, EventBooking

# Register the Event model
admin.site.register(Event)

# Register the EventBooking model
admin.site.register(EventBooking)
