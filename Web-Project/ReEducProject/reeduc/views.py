from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

connection = False

def index(request):
    return render(request, 'index.html', {'connection': connection})

def home(request):
    return render(request, 'home.html', {'connection': connection})

def login(request):
    return render(request, 'login.html', {'connection': connection})

def subscribe(request):
    return render(request, 'subscribe.html', {'connection': connection})

def view(request):
    return render(request, 'view.html', {'connection': connection})