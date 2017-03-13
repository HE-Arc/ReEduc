from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'connection': True})

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def subscribe(request):
    return render(request, 'subscribe.html')

def view(request):
    return render(request, 'view.html')