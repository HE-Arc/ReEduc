from django.shortcuts import render
from django.http import HttpResponse
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart

from django.shortcuts import render

connection = True

def index(request):
    return render(request, 'index.html', {'connection': connection})

def home(request):
    return render(request, 'home.html', {'connection': connection})

def login(request):
    return render(request, 'login.html', {'connection': connection})

def subscribe(request):
    return render(request, 'subscribe.html', {'connection': connection})

def view(request):
    data = [
        ['Year', 'Sales', 'Expenses'],
        [2004, 1000, 400],
        [2005, 1170, 460],
        [2006, 660, 1120],
        [2007, 1030, 540]
    ]
    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    chart = LineChart(data_source)
    context = {'chart': chart,'connection': connection}
    return render(request, 'view.html', context)

def homeSelected(request):
    return render(request, 'homeSelected.html', {'connection': connection})