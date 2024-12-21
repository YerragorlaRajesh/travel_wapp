# cab_booking/models.py
from django.db import models
from django.contrib.auth.models import User

class Cab(models.Model):
    cab_type = models.CharField(max_length=50)
    base_fare = models.DecimalField(max_digits=5, decimal_places=2)
    per_km_rate = models.DecimalField(max_digits=5, decimal_places=2)

class CabBooking(models.Model):
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    drop_location = models.CharField(max_length=100)
    pickup_time = models.DateTimeField()
    distance = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    estimated_fare = models.DecimalField(max_digits=8, decimal_places=2)
