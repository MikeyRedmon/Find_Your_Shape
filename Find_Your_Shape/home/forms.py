from django import forms
from .models import hittclasses, hiitbook


class ClassForm(forms.ModelForm):
    class Meta:
        model = hiitbook
        fields = ['name', 'focus', 'time']


class BookForm(forms.ModelForm):
    class Meta:
        model = hittclasses
        fields = ['name', 'trainer', 'focus']
