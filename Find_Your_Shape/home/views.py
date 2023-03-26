from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import hiitbook, hittclasses, PtClasses, SpinClasses
from .forms import BookingForm, BookingPT, NewUserForm, HittClassForm, SpinForm


# Return home


def home(request):
    return render(request, "home/home_page.html")


# Log In function


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
                return redirect("login")
            else:
                messages.error(request, "Invalid Username or passward")
                return redirect("login")
        else:
            messages.error(request, "Invalid Username or passward")
            return redirect("login")
    form = AuthenticationForm()
    return render(request, "home/login.html", context={"login_form": form})


# Log out function


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')


# Register Request


def register_request(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("register")
        else:
            messages.error(request, "Registration Failed, Please Try again")
            return redirect("register")
    return render(request, "home/register.html",
                  context={"register_form": form})


# Booking Page view

def booking(request):

    SpinClass = SpinClasses.objects.all()
    hittclass = hittclasses.objects.all()
    hiitbooks = hiitbook.objects.all()
    ptClass = PtClasses.objects.all()
    context = {
        'SpinClass': SpinClass,
        'ptClass': ptClass,
        'hittclass': hittclass,
        'hiitclasses':  hiitbooks,
    }
    return render(request, "home/booking_page.html", context)


# Booking view function

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


# Booking a PT Class Function


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


# Booking a Hiit Class


def hiitclass(request):

    if request.method == 'POST':
        form = HittClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")

    Hiit = HittClassForm()
    context = {
        'form': Hiit
    }

    return render(request, "home/bookingin.html", context)


# Booking a Spin Class


def SpinBooking(request):

    if request.method == 'POST':
        form = SpinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")

    Spin = SpinForm()
    context = {
        'form': Spin
    }

    return render(request, "home/bookingin.html", context)


#  Editing a Hiit Class


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


# Editing a Spin Class


def editingspin(request, item_id):
    item = get_object_or_404(SpinClasses, id=item_id)
    form = SpinForm(instance=item)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = SpinForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("booking")

    return render(request, 'home/editing.html', context)


# Editing a PT Session


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


# Editing a hiit session

def editinghiit(request, item_id):
    item = get_object_or_404(hiitbook, id=item_id)
    Book = HittClassForm(instance=item)
    context = {
        'form': Book
    }

    if request.method == 'POST':
        form = HittClassForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("booking")

    return render(request, 'home/editinghiit.html', context)


# Editing a Spin Session

def editingspin(request, item_id):
    item = get_object_or_404(SpinClasses, id=item_id)
    Book = SpinForm(instance=item)
    context = {
        'form': Book
    }

    if request.method == 'POST':
        form = SpinForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("booking")

    return render(request, 'home/editinghiit.html', context)


# Deleting a Hiit Class Modal popup

def deletehiit(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    Book = HittClassForm(instance=item)
    context = {
        'form': Book
    }
    return render(request, 'home/deletehiit.html', context)


# Deleting an Assessment Modal popup


def deleteassessment(request, item_id):
    ''''''
    item = get_object_or_404(hiitbook, id=item_id)
    Book = BookingPT(instance=item)
    context = {
        'form': Book
    }
    return render(request, 'home/deleteassessment.html', context)


# Deleting a PT session Modal popup


def deletept(request, item_id):
    item = get_object_or_404(PtClasses, id=item_id)
    Book = BookingPT(instance=item)
    context = {
        'form': Book
    }
    return render(request, 'home/deletept.html', context)


# Deleting a Spin class Modal popup


def deletespin(request, item_id):
    item = get_object_or_404(SpinClasses, id=item_id)
    Book = SpinForm(instance=item)
    context = {
        'form': Book
    }
    return render(request, 'home/deletespin.html', context)


# Delete functions for all models

def deleting(request, item_id):
    item = get_object_or_404(hiitbook, id=item_id)
    item.delete()
    return redirect("booking")


def deletingpt(request, item_id):
    item = get_object_or_404(PtClasses, id=item_id)
    item.delete()
    return redirect("booking")


def deletinghiit(request, item_id):
    item = get_object_or_404(hittclasses, id=item_id)
    item.delete()
    return redirect("booking")


def deletingspin(request, item_id):
    item = get_object_or_404(SpinClasses, id=item_id)
    item.delete()
    return redirect("booking")
