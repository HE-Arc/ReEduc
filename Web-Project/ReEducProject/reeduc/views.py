from django.shortcuts import render
from django.http import HttpResponse
from chartit import DataPool, Chart
from reeduc.models import PlayedGame

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
    # Step 1: Create a DataPool with the data we want to retrieve.
    datas = \
        DataPool(
            series=
            [{'options': {
                'source': PlayedGame.objects.all()},
                'terms': [
                    'date',
                    'needed_time',
                    'score']}
            ])

    # Step 2: Create the Chart object
    cht = Chart(
        datasource=datas,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'date': [
                    'needed_time',
                    'score']
            }}],
        chart_options=
        {'title': {
            'text': 'Score & Needed time graph'},
            'xAxis': {
                'title': {
                    'text': 'Date'}}})

    # Step 3: Send the chart object to the template.
    context = {'chart': cht,'connection': connection}
    return render(request, 'view.html', context)

def homeSelected(request):
    return render(request, 'homeSelected.html', {'connection': connection})