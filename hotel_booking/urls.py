from django.urls import path
from . import views

app_name = 'hotel_booking'

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),  # List of hotels
    path('<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),  # Hotel details
    path('<int:hotel_id>/book/', views.book_hotel, name='book_hotel'),  # Book a hotel
    path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),  # Booking confirmation (optional view)
]

