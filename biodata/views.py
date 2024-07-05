from django.shortcuts import render
from .forms import myform
from .models import Test
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def resume(request):
    return render(request,'resume.html')

def service(request):
    return render(request,'service.html')
    
def contact(request):
    if request.method=='POST':
        fm=myform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            sub=fm.cleaned_data['sub']
            msg=fm.cleaned_data['msg']
            con=Test(name=nm,email=em,sub=sub,msg=msg)
            con.save()
    else :
        fm=myform()
    return render(request,'contact.html',{'form':fm})