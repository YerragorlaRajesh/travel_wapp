from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Booking
from travel_wapp.utils import get_rajesh_user
from datetime import datetime

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_booking/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotel_booking/hotel_detail.html', {'hotel': hotel})

def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':
        check_in_date = datetime.strptime(request.POST['check_in_date'], '%Y-%m-%d').date()
        check_out_date = datetime.strptime(request.POST['check_out_date'], '%Y-%m-%d').date()
        guests = int(request.POST['guests'])
        
        # Calculate number of nights
        nights = (check_out_date - check_in_date).days
        total_price = hotel.price_per_night * nights

        booking = Booking.objects.create(
            hotel=hotel,
            user=get_rajesh_user(),  # Using Rajesh user
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guests=guests,
            total_price=total_price
        )
        return redirect('hotel_booking:booking_confirmation', booking_id=booking.id)

    return render(request, 'hotel_booking/book_hotel.html', {'hotel': hotel})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'hotel_booking/booking_confirmation.html', {'booking': booking})