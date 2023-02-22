from django.shortcuts import render
from .models import hiitbook, hittclasses

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def booking(request):
    hiitbooks = hiitbook.objects.all()
    context = {
        'hiitclasses':  hiitbooks
    }
    return render(request, "home/booking_page.html", context)


def bookingin(request):
    return render(request, "home/bookingin.html")
