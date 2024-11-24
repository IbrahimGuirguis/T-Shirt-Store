from django.shortcuts import render
from .models import ContactForm, ContactInfo

def contact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    data = ContactForm(first_name=first_name, last_name=last_name, email=email, message=message)
    if request.method == "POST":
        data.save()
    contact_info = ContactInfo.objects.get(pk=1)
    return render(request, 'Contact.html', {'contact_info':contact_info})