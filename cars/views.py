def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.save()

            # 1. EMAIL TO YOU - THE ADMIN
            subject_admin = f'New Booking: {car.brand} {car.name}'
            message_admin = f"""
New booking request for SN TRANSPORT!

Car: {car.brand} {car.name}
Price: ${car.price_per_day}/day

Customer Details:
Name: {booking.customer_name}
Phone: {booking.customer_phone}
Email: {booking.customer_email}
Pickup: {booking.pickup_date}
Return: {booking.return_date}
Message: {booking.message}

Go to admin to approve: https://sntransport-rw.onrender.com/admin/cars/booking/{booking.id}/change/
            """
            send_mail(
                subject_admin,
                message_admin,
                settings.DEFAULT_FROM_EMAIL,  # from: itdann12@gmail.com
                [settings.DEFAULT_FROM_EMAIL],  # to: you
                fail_silently=False,
            )

            # 2. EMAIL TO CUSTOMER - CONFIRMATION
            subject_customer = f'Booking Received - {car.brand} {car.name} | SN Transport'
            message_customer = f"""
Hi {booking.customer_name},

Thank you for booking with SN TRANSPORT & LOGISTICS LTD!

We received your request for:
Car: {car.brand} {car.name}
Pickup Date: {booking.pickup_date}
Return Date: {booking.return_date}

What happens next?
Our team will contact you at {booking.customer_phone} within 2 hours to confirm your booking and payment details.

For questions call us: 0788626377

Best regards,  
SN Transport Team  
Kigali, Rwanda
            """
            send_mail(
                subject_customer,
                message_customer,
                settings.DEFAULT_FROM_EMAIL,  # from: itdann12@gmail.com
                [booking.customer_email],  # to: customer
                fail_silently=False,
            )

            return render(request, 'cars/book_success.html', {'car': car, 'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'cars/book.html', {'form': form, 'car': car})