from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import hiitbook, hittclasses, PtClasses
from .forms import BookingForm, BookingPT, NewUserForm

# Create your views here.


def home(request):
    return render(request, "home/home_page.html")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in {username}")
                return redirect("booking")
            else:
                messages.error(request, "Invalid Username or passward")
        else:
            messages.error(request, "Invalid Username or passward")
    form = AuthenticationForm()
    return render(request, "home/login.html",
                context={"login_form":form})




def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("booking")
        messages.error(request, "Registration Failed, Please Try again")
    form = NewUserForm()
    return render(request, "home/register.html",
                  context={"register_form": form})


def booking(request):

    hittclass = hittclasses.objects.all()
    hiitbooks = hiitbook.objects.all()
    ptClass = PtClasses.objects.all()
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

    if request.method == 'POST':
        form = BookingPT(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")

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


def editingpt(request, item_id):
    item = get_object_or_404(PtClasses, id=item_id)
    Book = BookingPT(instance=item)
    context = {
        'form': Book
    }

    if request.method == 'POST':
        formSes = BookingPT(request.POST, instance=item)
        if formSes.is_valid():
            formSes.save()
            return redirect("booking")

    return render(request, 'home/editingpt.html', context)


def deleting(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    item.delete()
    return redirect("booking")


def deletingpt(request, item_id):
    item = get_object_or_404(PtClasses, id=item_id)
    item.delete()
    return redirect("booking")
