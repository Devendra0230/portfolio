from django.contrib import admin
from .models import Test
# Register your models here.
@admin.register(Test)
class mdt(admin.ModelAdmin):
    list_display=['id','name','email','sub','msg']