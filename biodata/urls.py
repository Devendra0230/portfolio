from django.urls import path

from biodata import views

urlpatterns = [
    path('',views.home , name='home'),
    path('About/',views.about ,name='about'),
    path('Service/',views.service ,name='service'),
    path('Resume/',views.resume , name='resume'),
    path('Contact/',views.contact, name='contact')
]