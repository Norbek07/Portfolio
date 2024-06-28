from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            new_content = Contact(name=name, email=email, content=content)
            new_content.save()
            messages.success(request,"your messages succesfully sent!")
            return HttpResponseRedirect(reverse('home-page'))

            return render(request, 'contact.html', {'success': True})
        except:
            # Feedback message for error
            return render(request, 'contact.html', {'error': True})

    return render(request, 'contact.html')
