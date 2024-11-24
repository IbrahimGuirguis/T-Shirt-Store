from django.shortcuts import render
from .models import SignUP

def login(request):
    return render(request, 'Login.html')

def sign_up(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    data = SignUP(username=username, email=email, password=password, confirm_password=confirm_password)
    if request.method == "POST":
        data.save()
    return render(request, 'SignUp.html')
