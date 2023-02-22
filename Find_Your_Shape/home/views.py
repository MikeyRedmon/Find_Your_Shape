from django.shortcuts import render, redirect
from .models import hiitbook, hittclasses

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        trainer = request.POST.get('item_trainer')
        focus = request.POST.get('item_focus')
        time = request.POST.get('item_time')
        hittclasses.objects.Create(name=name, trainer=trainer, focus=focus, time=time)
        return redirect('booking')
    hiitbooks = hiitbook.objects.all()
    context = {
        'hiitclasses':  hiitbooks
    }
    return render(request, "home/booking_page.html", context)


def bookingin(request):
    return render(request, "home/bookingin.html")
