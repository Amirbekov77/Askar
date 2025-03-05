# reservations/forms.py
from django import forms
from .models import Reservation
from .models import Customer, Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date', 'status']
