"""Find_Your_Shape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    # Admin

    path('admin/', admin.site.urls),

    # Basic Views

    path('', views.home, name='home'),
    path('booking', views.booking, name='booking'),
    path('bookingin', views.bookingin, name='bookingin'),
    path('bookinginSes', views.bookinginSes, name='bookinginSes'),
    path('hittclasses', views.hiitclass, name='hiitclasses'),
    path('spinclasses', views.SpinBooking, name='spinclasses'),

    # Editing items views

    path('editing/<item_id>', views.editing, name='edit'),
    path('editinghiit/<item_id>', views.editinghiit, name='edit'),
    path('editingspin/<item_id>', views.editingspin, name='editspin'),
    path('editingpt/<item_id>', views.editingpt, name='editpt'),

    # Deleting Modals

    path('deletehiit/<item_id>', views.deletehiit, name='deletehiit'),
    path('deleteassessment/<item_id>', views.deleteassessment,
         name='deleteassessment'),
    path('deletept/<item_id>', views.deletept, name='deletept'),
    path('deletespin/<item_id>', views.deletespin, name='deletespin'),

    # Deleting Items

    path('deleting<item_id>', views.deleting, name='deleting'),
    path('deletingpt<item_id>', views.deletingpt, name='deletingpt'),
    path('deletehiit<item_id>', views.deletinghiit, name='deletinghiit'),
    path('deletingspin<item_id>', views.deletingspin, name='deletingspin'),

    # Register and log in paths

    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name="logout")
]
