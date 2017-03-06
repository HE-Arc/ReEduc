from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Game(models.Model):
    name=models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

class Player(models.Model):
    STRONG_ARM_CHOICE= (
        ('R', 'RIGHT'),
        ('L', 'LEFT'),
    )
    GENDER_CHOICE = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    size = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=1,choices=STRONG_ARM_CHOICE)
    strong_arm = models.CharField(max_length=1,choices=GENDER_CHOICE)
    handicap = models.CharField(max_length=1000)
    birthdate = models.DateField()
    spec_id = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True,max_length=15)

class PlayedGame(models.Model):
    game= models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    comments = models.CharField(max_length=1000)
    needed_time = models.IntegerField()
    score = models.IntegerField()
    errors = models.IntegerField()

