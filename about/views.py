from django.shortcuts import render
from .models import AboutUs

def about(request):
    about_us = AboutUs.objects.get(pk=1) 
    return render(request, 'About.html', {'about_us':about_us})
