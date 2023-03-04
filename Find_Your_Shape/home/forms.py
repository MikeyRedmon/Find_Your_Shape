from django import forms
from .models import hittclasses, PtClasses, users


class BookingForm(forms.ModelForm):
    class Meta:
        model = hittclasses
        fields = ['name', 'trainer', 'focus']


class BookingPT(forms.ModelForm):
    class Meta:
        model = PtClasses
        fields = ['name', 'trainer', 'focus', 'time']
        

class LogIn(forms.ModelForm):
    class Meta:
        model = users
        fields = ['name', 'password']
