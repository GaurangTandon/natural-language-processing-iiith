from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.introduction, name='chunking.home'),
    url(r'^introduction/$', views.introduction, name='chunking.introduction'),
    url(r'^experiment/$', views.experiment, name='chunking.experiment'),
    url(r'^theory/$', views.theory, name='chunking.theory'),
    url(r'^objective/$', views.objective, name='chunking.objective'),
    url(r'^procedure/$', views.procedure, name='chunking.procedure'),
    url(r'^readings/$', views.readings, name='chunking.readings'),
]