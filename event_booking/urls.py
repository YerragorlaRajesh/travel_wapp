from django.urls import path
from . import views

app_name = 'event_booking'

urlpatterns = [
    path('', views.event_list, name='event_list'),  # List of events
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # Event details
    path('<int:event_id>/book/', views.book_event, name='book_event'),  # Book event tickets
    path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),  # Booking confirmation (optional view)
]
