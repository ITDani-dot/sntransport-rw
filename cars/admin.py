from django.contrib import admin
from .models import Car, Booking

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'price_per_day', 'seats', 'is_available')
    list_filter = ('brand', 'is_available', 'transmission')
    search_fields = ('name', 'brand')
    list_editable = ('is_available',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'car', 'pickup_date', 'return_date', 'is_confirmed', 'created_at')
    list_filter = ('is_confirmed', 'pickup_date', 'car')
    search_fields = ('customer_name', 'customer_email', 'customer_phone')
    list_editable = ('is_confirmed',)
    readonly_fields = ('created_at',)