from django.conf import settings
from django.core import mail
from django.shortcuts import redirect, render

from .forms import myform
from .models import ContactForm


def home(request):
    fm = myform(request.POST)
    return render(request, 'home.html', {'form': fm})
    

def contact(request):
    if request.method == 'POST':
        fm = myform(request.POST)
        if fm.is_valid():
            fm.save()
            nm = request.POST['name']
            em = request.POST['email']
            sub = request.POST['sub']
            msg = request.POST['msg']
            
            message = f'''Feedback from: {nm}
Subject: {sub}
User contact: {em}

User msg: {msg}
            '''
            to_email = 'devendralodhi192@gmail.com'
            
            try:
                mail.send_mail('Feedback from Portfolio', message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)
            except Exception as e:
                print(f"Failed to send email: {e}")
            return redirect('home')
    else:
        fm = myform()
    return redirect(home)
    
    
