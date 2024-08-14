from django.contrib import admin

from .models import ContactForm


# Register your models here.
@admin.register(ContactForm)
class mdt(admin.ModelAdmin):
    list_display=['id','name','email','sub','msg']