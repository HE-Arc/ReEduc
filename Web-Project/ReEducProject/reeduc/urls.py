from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home/$', views.home, name="home"),
    url(r'^home/([0-9]*)/$', views.view, name="view"),
    url(r'^login', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),
    url(r'^subscribe', views.subscribe, name="subscribe"),
    url(r'^account', views.account, name="account"),

]

