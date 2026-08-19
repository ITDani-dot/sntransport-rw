from django.db import models
from cars.models import Car
import africastalking

def send_booking_sms(phone, message):
    username = "sandbox" # Change to your AT username
    api_key = "your_api_key" # Get from africastalking.com
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    
    if not phone.startswith('+'):
        phone = '+250' + phone.lstrip('0') # Rwanda format
    sms.send(message, [phone])

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        # Send SMS when booking is created
        if is_new:
            message = f"Hi {self.customer_name}, your booking for {self.car} is received. We will confirm soon."
            send_booking_sms(self.customer_phone, message)
    
    def __str__(self):
        return f"{self.customer_name} - {self.car}"
        from django.utils import timezone

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField(blank=True, null=True)
    pickup_date = models.DateField()
    return_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.car.name}"