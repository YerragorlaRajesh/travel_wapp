# event_booking/models.py
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    event_date = models.DateField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_tickets = models.IntegerField(default=100)  # Add a default value for total tickets
    tickets_sold = models.IntegerField(default=0)   

class EventBooking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
