from django.urls import path
from . import views

app_name = 'cab_booking'

urlpatterns = [
    path('', views.cab_list, name='cab_list'),  # List of cabs
    path('<int:cab_id>/estimate/', views.estimate_fare, name='estimate_fare'),  # Estimate fare
    path('<int:cab_id>/book/', views.book_cab, name='book_cab'),  # Book a cab
    path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),  # Booking confirmation (optional view)
]

