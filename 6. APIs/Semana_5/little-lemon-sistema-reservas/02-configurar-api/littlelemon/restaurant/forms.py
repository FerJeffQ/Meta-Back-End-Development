from django.forms import ModelForm
from .models import Booking, Menu

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"