from django.urls import path

from biodata import views

urlpatterns = [
    path('',views.home , name='home'),
]