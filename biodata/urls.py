from django.urls import path

from biodata import views

from .views import *

urlpatterns = [
    path('',views.home , name='home'),
    path('Contact/',views.contact, name='contact'),
    ]