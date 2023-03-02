from django.shortcuts import render, redirect, get_object_or_404
from .models import hiitbook, hittclasses, PtClasses
from .forms import BookingForm, BookingPT

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def booking(request):

    if request.method == 'POST':
        form = BookingPT(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")

    hittclass = hittclasses.objects.all()
    hiitbooks = hiitbook.objects.all()
    ptClass = PtClasses
    context = {
        'ptClass': ptClass,
        'hittclass': hittclass,
        'hiitclasses':  hiitbooks,
    }
    return render(request, "home/booking_page.html", context)


def bookingin(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")

    formSes = BookingForm()
    context = {
        'form': formSes
    }
    return render(request, "home/bookingin.html", context)


def bookinginSes(request):
    Book = BookingPT()
    context = {
        'form': Book
    }
    return render(request, "home/bookingin.html", context)


def editing(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    formSes = BookingForm(instance=item)
    context = {
        'form': formSes
    }

    if request.method == 'POST':
        formSes = BookingForm(request.POST, instance=item)
        if formSes.is_valid():
            formSes.save()
            return redirect("booking")

    return render(request, 'home/editing.html', context)


def deleting(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    item.delete()
    return redirect("booking")
