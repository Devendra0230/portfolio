from django import forms
class myform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'name':'name','id':'name','placeholder':'your name','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'name':'email','id':'email','placeholder':'your email','class':'form-control'}))
    sub=forms.CharField(widget=forms.TextInput(attrs={'name':'subject','id':'subject','placeholder':'subject','class':'form-control'}))
    msg=forms.CharField(widget=forms.Textarea(attrs={'name':'message','class':'form-control','placeholder':'Message'}))