from chartit import DataPool, Chart
from reeduc.models import PlayedGame, Player
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db.models import Max
from django.db.models import Min


#Website authentification pages
def logout(request):
    auth_logout(request)
    return render(request, 'login.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    actualUser = authenticate(username=username, password=password)
    if actualUser is not None:
        auth_login(request, actualUser)
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')

def subscribe(request):

    #Récupération des infos du formulaires
    user_username = request.POST.get('username')
    user_password = request.POST.get('password')
    user_email = request.POST.get('email')
    user_firstname = request.POST.get('firstname')
    user_lastname = request.POST.get('lastname')

    player_birthdate = request.POST.get('birthdate')
    player_phone = request.POST.get('phone')
    player_gender = request.POST.get('gender')
    player_height = request.POST.get('height')
    player_weight = request.POST.get('weight')

    #Fingers
    player_thumbleft = request.POST.get('thumbleft', False)
    player_forefingerleft = request.POST.get('forefingerleft', False)
    player_middlefingerleft = request.POST.get('middlefingerleft', False)
    player_ringfingerleft = request.POST.get('ringfingerleft', False)
    player_littlefingerleft = request.POST.get('littlefingerleft', False)

    player_thumbright = request.POST.get('thumbright',False)
    player_forefingerright = request.POST.get('forefingerright',False)
    player_middlefingerright = request.POST.get('middlefingerright',False)
    player_ringfingerright = request.POST.get('ringfingerright',False)
    player_littlefingerright = request.POST.get('littlefingerright', False)

    #Arms
    player_leftarm = request.POST.get('leftarm', False)
    player_rightarm = request.POST.get('rightarm', False)
    player_strongarm=request.POST.get('player_strongarm')

    if user_username is not None: # TODO Devra être remplacé par une validation de formulaire
        if not User.objects.filter(username=user_username).exists():
            if not User.objects.filter(email=user_email).exists():

                HandicapsVals = []
                HandicapsVals.append(player_thumbleft)
                HandicapsVals.append(player_forefingerleft)
                HandicapsVals.append(player_middlefingerleft)
                HandicapsVals.append(player_ringfingerleft)
                HandicapsVals.append(player_littlefingerleft)
                HandicapsVals.append(player_thumbright)
                HandicapsVals.append(player_forefingerright)
                HandicapsVals.append(player_middlefingerright)
                HandicapsVals.append(player_ringfingerright)
                HandicapsVals.append(player_littlefingerright)
                HandicapsVals.append(player_leftarm)
                HandicapsVals.append(player_rightarm)

                strHandicaps =""
                for i in range(len(HandicapsVals)):
                    if HandicapsVals[i]:
                        strHandicaps += "F;"
                    else:
                        strHandicaps += "T;"
                genderValue=''
                if player_gender=='Man':
                    genderValue='M'
                else:
                    genderValue='F'

                strongArmValue = ''
                if player_strongarm == 'Left':
                    strongArmValue = 'L'
                else:
                    strongArmValue = 'R'

                # Create a new User
                user = User(
                    first_name=user_firstname,
                    is_staff=True,
                    is_superuser=True,
                    last_name=user_lastname,
                    username=user_username,
                    email=user_email
                )
                user.set_password(user_password)
                user.save()

                #Generate spec_id
                player_spec_id = get_random_string(length=6)
                while(Player.objects.filter(spec_id=player_spec_id).exists()):
                    player_spec_id=get_random_string(length=6)

                # Create a new Player (player is an extention of user)
                p = Player(user=User.objects.get(username=user_username),
                           size=player_height,
                           weight=player_weight,
                           gender=genderValue,
                           strong_arm=strongArmValue,
                           handicap=strHandicaps,
                           birthdate=player_birthdate,
                           spec_id=player_spec_id,
                           phone_number=player_phone,
                           )
                p.save()

                return render(request, 'login.html')
    else:
        return render(request, 'subscribe.html')



#Website content pages
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

# Best decorator ever ->
@login_required(login_url='/login/')
def view(request):
    # Get actual connected user and get corresponding player datas
    actualPlayer=Player.objects.get(user_id=request.user.id)
    # Get all played games by this user
    playedGames=PlayedGame.objects.filter(player_id=actualPlayer, game_id=1)
    # Step 1: Create a DataPool with the data we want to retrieve.
    datas = \
        DataPool(
            series=
            [{'options': {
                'source': playedGames},
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
    return render(request, 'view.html', {'chart': cht,'playedGames':playedGames})

@login_required(login_url='/login/')
def homeSelected(request):
    return render(request, 'homeSelected.html')

@login_required(login_url='/login/')
def account(request):
    actual_user= User.objects.get(pk=request.user.id)
    actual_player = Player.objects.get(user_id=request.user.id)
    played_games = PlayedGame.objects.filter(player_id=actual_player.pk)
    best_score=PlayedGame.objects.filter(player_id=actual_player.pk).aggregate(Max('score'))
    max_score=best_score.get('score__max')
    best_time = PlayedGame.objects.filter(player_id=actual_player.pk).aggregate(Min('needed_time'))
    min_time=best_time.get('needed_time__min')
    return render(request, 'account.html', {'actual_user': actual_user,
                                            'actual_player':actual_player,
                                            'played_games':played_games,
                                            'max_score': max_score,
                                            'min_time':min_time})
# TODO Récupérer la valeur du jeu sélectionner dans home et remplace le game_id=1 dans la fonction view ci-dessus pas le bon id