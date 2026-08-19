from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_phone', 'customer_email', 'pickup_date', 'return_date', 'message']
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any special requests?'}),
            'customer_name': forms.TextInput(attrs={'placeholder': 'Full Names'}),
            'customer_phone': forms.TextInput(attrs={'placeholder': '+250 7XX XXX'}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
        }