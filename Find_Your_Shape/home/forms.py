from django import forms
from .models import hittclasses, PtClasses


class BookingForm(forms.ModelForm):
    class Meta:
        model = hittclasses
        fields = ['name', 'trainer', 'focus']


class BookingPT(forms.ModelForm):
    class Meta:
        model = PtClasses
        fields = ['name', 'trainer', 'focus', 'time']
