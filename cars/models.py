from django.db import models  # <- THIS LINE WAS MISSING

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(default="Luxury car available for rent")
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    seats = models.IntegerField(default=5)  # <- ADD THIS
    transmission = models.CharField(max_length=50, default="Automatic")
    fuel = models.CharField(max_length=50, default="Petrol")
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.name}"


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()
    pickup_date = models.DateField()
    return_date = models.DateField()
    message = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.car.name}"