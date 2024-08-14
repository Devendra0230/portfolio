from django import forms
from django.core.validators import EmailValidator

from .models import ContactForm


class myform(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"
        widgets = {
            "name" : forms.TextInput(attrs={'name':'name','id':'name','placeholder':'Your Name','class':'form-control'}),
            "email": forms.EmailInput(attrs={'name':'email','id':'email','placeholder':'Your Email','class':'form-control'}),
            "sub" : forms.TextInput(attrs={'name':'subject','id':'subject','placeholder':'Subject','class':'form-control'}),
            "msg": forms.Textarea(attrs={'name':'message','class':'form-control','placeholder':'Message'})
        }