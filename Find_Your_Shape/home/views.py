from django.shortcuts import render, redirect, get_object_or_404
from .models import hiitbook, hittclasses
from .forms import ClassForm, BookForm

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def booking(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
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


def editing(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('booking')

    form = ClassForm(instance=item)
    context = {
        'form': ClassForm
    }
    return render(request, 'home/editing.html', context)
