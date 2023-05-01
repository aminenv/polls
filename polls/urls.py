from django.conf.urls import urls
from . import views

urlpatterns = [
    url(r'^accounts/register/?$', views.register, name='register'),
    url(r'^accounts/whoami/?$', views.whoami, name='whoami'),
    url(r'^$', views.index, name='index'),
]
