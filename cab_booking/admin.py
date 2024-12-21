from django.contrib import admin
from .models import Cab, CabBooking

# Register the Cab model
admin.site.register(Cab)

# Register the CabBooking model
admin.site.register(CabBooking)
