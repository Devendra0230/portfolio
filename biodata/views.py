from django.conf import settings
from django.core import mail
from django.shortcuts import render

from .forms import myform
from .models import Test


def home(request):
    if request.method=='POST':
        fm=myform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            sub=fm.cleaned_data['sub']
            msg=fm.cleaned_data['msg']
            con=Test(name=nm,email=em,sub=sub,msg=msg)
            con.save()
            msg=f'''
            Feedbcak From : {nm}
            User Mail : {em}
            Subject : {sub}

                {msg}
            '''
        send_mail = mail.send_mail(sub,msg,settings.EMAIL_HOST_USER, ['devendralodhi192@gmail.com'],fail_silently = False)
    else :
        fm=myform()
    return render(request,'home.html',{'form':fm})
