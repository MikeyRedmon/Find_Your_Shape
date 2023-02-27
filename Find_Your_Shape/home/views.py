from django.shortcuts import render, redirect, get_object_or_404
from .models import hiitbook, hittclasses, PtClasses
from .forms import BookingForm

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")

    hittclass = hittclasses.objects.all()
    hiitbooks = hiitbook.objects.all()
    context = {
        'hittclass': hittclass,
        'hiitclasses':  hiitbooks,
    }
    return render(request, "home/booking_page.html", context)


def bookingin(request):
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, "home/bookingin.html", context)


def bookingin(request):
    form = BookingPT()
    context = {
        'form': form
    }
    return render(request, "home/bookingin.html", context)

def editing(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    form = BookingForm(instance=item)
    context = {
        'form': form
    }
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("booking")

    return render(request, 'home/editing.html', context)

def deleting(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    item.delete()
    return redirect("booking")