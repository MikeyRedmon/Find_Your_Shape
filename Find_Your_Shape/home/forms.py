from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import hittclasses, PtClasses, hiitbook, SpinClasses

# Form Used to Book Assessments


class BookingForm(forms.ModelForm):
    class Meta:
        model = hittclasses
        fields = ['name', 'trainer', 'focus']


# Form used to Book Spin Clases

class SpinForm(forms.ModelForm):
    class Meta:
        model = SpinClasses
        fields = ['name', 'genre', 'time']


# Form Used to Book Personal Training Sessions


class BookingPT(forms.ModelForm):
    class Meta:
        model = PtClasses
        fields = ['name', 'trainer', 'focus', 'time']


# Form used to book HIIT sessions

class HittClassForm(forms.ModelForm):
    class Meta:
        model = hiitbook
        fields = ['name', 'focus', 'time']

# New User Form


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
