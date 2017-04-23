from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home/$', views.home, name="home"),
    # XXX home/1 ? views.view ?? c'est diffile à comprendre.
    url(r'^home/([0-9]*)/$', views.view, name="view"),
    url(r'^subscribe', views.subscribe, name="subscribe"),
    url(r'^informations', views.informations, name="informations"),
    # XXX tout ça est fournit par Django gratuitement.
    url(r'^account', views.account, name="account"),
    url(r'^login', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),

]

