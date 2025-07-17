from django.shortcuts import render

from django.http import HttpResponse
from .models import Contact

from django.shortcuts import HttpResponse

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')

def submit_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(name=name, email=email, message=message)
        
        return HttpResponse(f"Thank you, {name}! Your message has been saved.")

    return HttpResponse("Invalid Request")

def contact_list(request):
    contacts = Contact.objects.all()  # Fetch all contacts
    return render(request, 'contact_list.html', {'contacts': contacts})




