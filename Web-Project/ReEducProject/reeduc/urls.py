from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^home', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^login', TemplateView.as_view(template_name='login.html'), name="login"),
    url(r'^subscribe', TemplateView.as_view(template_name='subscribe.html'), name="subscribe"),
    url(r'^view', TemplateView.as_view(template_name='view.html'), name="view"),
]
