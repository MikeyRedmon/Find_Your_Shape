from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home/home_page.html")


def booking(request):
    return render(request, "home/booking_page.html")