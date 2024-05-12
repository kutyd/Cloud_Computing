from django.shortcuts import render, redirect
from cloud_odev.models import Kisi
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        email_exists = False
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if  not Kisi.objects.filter(KisiMail = email).exists():
            new_user = Kisi.objects.create(KisiMail=email,KisiPassword=password)
            email_exists = True
            return render(request,'login.html',{'email': email,'email_exists':email_exists,})
        elif Kisi.objects.filter(KisiMail=email).exists():
            return render(request,'welcome.html',{'email': email})
    
    return render(request,'login.html')

