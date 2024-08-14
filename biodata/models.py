from django.db import models


class ContactForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    sub=models.CharField(max_length=100)
    msg=models.CharField(max_length=100)
    