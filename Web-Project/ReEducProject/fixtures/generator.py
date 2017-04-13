# -*- coding: utf-8 -*-
import json
# Make it work for Python 2+3 and with Unicode
import io
import random
from collections import OrderedDict

from django.conf import settings
from django.contrib.auth.hashers import make_password
settings.configure()


pwd = make_password('1234')

print(pwd)

try:
    to_unicode = unicode
except NameError:
    to_unicode = str




def GenerateGame():
    f = []
    name = ["Coordinate Finger", "Coordinate arms", "Coordinate hand", "Coordinate all"]
    for i in range(0, 4):
        a = (("name", name[i]), ("description", "Using " + name[i]))
        b = OrderedDict(a)
        c = (('model', 'reeduc.Game'), ('pk', i), ("fields", b))
        d = OrderedDict(c)
        f.append(d)
    return f


def GenerateUser():
    f = []
    username = ["cyrilmanuel", "user1", "user2", "user3"]
    fname = ["cyril", "user", "user", "user"]
    lname = ["jeanneret", "user", "user", "user"]
    for i in range(0, 4):
        a = (("username", username[i]), ("first_name", fname[i]), ("last_name", lname[i]), ("is_active", True),
             ("is_superuser", False),
             ("is_staff", True), ("last_login", "2017-03-13T10:28:35Z"), ("groups", []), ("user_permissions", []),
             ("password", str(make_password('1234'))),
             ("email", username[i] + "@gmail.com"),
             ("date_joined", "2017-03-13T08:28:35Z"))
        b = OrderedDict(a)
        c = (('model', 'auth.user'), ('pk', i), ("fields", b))
        d = OrderedDict(c)
        f.append(d)
    return f

def GeneratePlayer():
    f = []
    for i in range(0, 4):
        a = (("size", random.randint(150, 210)), ("weight", random.randint(69, 105)),("gender","M"),
             ("strong_arm", "L"),
             ("handicap", "T:T:T:T:T:T:T:T:T:T:F:F"),
             ("birthdate", str(random.randint(1990, 2010))+"-"+str(random.randint(1, 12)).zfill(2)+"-"+str(random.randint(1, 25)).zfill(2)),
              ("user_id", i), ("spec_id", "testee"+str(i)),("phone_number", "0775142122"))
        b = OrderedDict(a)
        c = (('model', 'reeduc.Player'), ('pk', i), ("fields", b))
        d = OrderedDict(c)
        f.append(d)
    return f

def GeneratePlayed():
    f = []
    for i in range(0, 120):
        a = (("game", random.randint(0, 3)), ("player", random.randint(0, 3)),
             ("comments", "Beaucoup d'erreurs ont \u00e9t\u00e9 d\u00e9tect\u00e9es avec l'index"),
             ("needed_time", random.randint(100, 200)),
             ("score", random.randint(0, 3000)), ("date", str(random.randint(1990, 2010))+"-"+str(random.randint(1, 12)).zfill(2)+"-"+str(random.randint(1, 25)).zfill(2)+"T17:41:28+00:00"), ("errors", random.randint(0, 20)))
        b = OrderedDict(a)
        c = (('model', 'reeduc.playedgame'), ('pk', i), ("fields", b))
        d = OrderedDict(c)
        f.append(d)
    return f


def GeneratorResultData():
    data = []
    data += GenerateGame() + GenerateUser() + GeneratePlayer() + GeneratePlayed()
    return data
# Write JSON file
with io.open('initial_data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(GeneratorResultData(),
                      indent=1, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('initial_data.json') as data_file:
    data_loaded = json.load(data_file)

