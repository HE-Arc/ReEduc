from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home', views.home, name="home"),
   # url(r'^home/(?P<pk>/$', views.homeSelected, name='homeSelected'),
    url(r'^login', views.login, name="login"),
    url(r'^subscribe', views.subscribe, name="subscribe"),
    url(r'^view', views.view, name="view"),
]
