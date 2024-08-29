from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('creer', views.creer),
    path('test', views.test),
    path('logout', views.deconnexion),
    path('espace-agent', views.home),

]