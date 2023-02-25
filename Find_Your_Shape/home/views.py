from django.shortcuts import render, redirect, get_object_or_404
from .models import hiitbook, hittclasses
from .forms import ClassForm, BookForm

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        trainer = request.POST.get('item_trainer')
        focus = request.POST.get('item_focus')
        hittclasses.objects.create(name=name, trainer=trainer, focus=focus)
        return redirect("booking")

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
    form = BookForm(instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('booking')

    form = ClassForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'home/editing.html', context)
