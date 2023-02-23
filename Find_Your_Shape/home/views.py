from django.shortcuts import render, redirect
from .models import hiitbook, hittclasses
from .forms import ClassForm

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def booking(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')

    hittclass = hittclasses.objects.all()
    hiitbooks = hiitbook.objects.all()
    context = {
        'hittclass': hittclass,
        'hiitclasses':  hiitbooks,
    }
    return render(request, "home/booking_page.html", context)


def bookingin(request):
    context = {
        'form': ClassForm
    }
    return render(request, "home/bookingin.html", context)
