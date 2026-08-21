from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Car, Booking
from .forms import BookingForm


def home(request):
    cars = Car.objects.filter(is_available=True)
    context = {
        'cars': cars,
        'company_name': 'SN TRANSPORT & LOGISTICS LTD',
        'slogan': 'is committed to providing safe, reliable, and premium transport solutions in Rwanda.',
        'location': 'Kigali, Rwanda',
        'phone': '0788626377'
    }
    return render(request, 'cars/home.html', context)


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/book.html', {'car': car})  # using book.html for details too


def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.save()

            # SEND EMAIL TO YOU WHEN SOMEONE BOOKS
            subject = f'New Booking: {car.brand} {car.name}'
            message = f"""
New booking request!

Car: {car.brand} {car.name}
Customer: {booking.customer_name}
Phone: {booking.customer_phone}
Email: {booking.customer_email}
Pickup: {booking.pickup_date}
Return: {booking.return_date}
Message: {booking.message}

Go to admin to approve: https://sntransport-rw.onrender.com/admin/cars/booking/{booking.id}/change/
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,  # from email
                [settings.DEFAULT_FROM_EMAIL],  # to: you
                fail_silently=False,
            )

            return render(request, 'cars/book_success.html', {'car': car, 'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'cars/book.html', {'form': form, 'car': car})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'cars/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'cars/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')