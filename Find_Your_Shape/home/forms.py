from django import forms
from .models import hittclasses


class BookingForm(forms.ModelForm):
    class Meta:
        model = hittclasses
        fields = ['name', 'trainer', 'focus']
