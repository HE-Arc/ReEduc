from chartit import DataPool, Chart
from reeduc.models import PlayedGame
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Variable example to pass to the templates
VarExampleToPassToTemplate = True

#Authentification part
def logout(request):
    auth_logout(request)
    return render(request, 'login.html', {'var': VarExampleToPassToTemplate})

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return render(request, 'home.html', {'var': VarExampleToPassToTemplate})
    else:
        return render(request, 'login.html', {'var': VarExampleToPassToTemplate})

def subscribe(request):
    return render(request, 'subscribe.html', {'var': VarExampleToPassToTemplate})


#Website Pages
def index(request):
    return render(request, 'index.html', {'var': VarExampleToPassToTemplate})

@login_required(login_url='/reeduc/login/')
def home(request):
    return render(request, 'home.html', {'var': VarExampleToPassToTemplate})

# Best decorator ever ->
@login_required(login_url='/reeduc/login/')
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
    context = {'chart': cht}
    return render(request, 'view.html', context)

@login_required(login_url='/reeduc/login/')
def homeSelected(request):
    return render(request, 'homeSelected.html', {'connection': VarExampleToPassToTemplate})