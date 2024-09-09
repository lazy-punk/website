from django.shortcuts import render, HttpResponse
import psycopg2
from .models import ContactMessage
# Create your views here.


def home(request):
    return render(request, 'my_app/index.html')


def greeting(request, name):
    return HttpResponse(f"Hello, {name}!")


def contact(request):
    return render(request, 'my_app/contact.html')


def features(request):
    return render(request, 'my_app/features.html')


def usage(request):
    return render(request, 'my_app/usage.html')


def installation(request):
    return render(request, 'my_app/installation.html')


def contributing(request):
    return render(request, 'my_app/contributing.html')


def licenses(request):
    return render(request, 'my_app/license.html')


def form_submitted(request):
    return render(request, 'my_app/form_submitted.html')


def contact_input(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return render(request, 'my_app/form_submitted.html')
    return render(request, 'my_app/contact.html')
