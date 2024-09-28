from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('creer', views.creer_nouveau_visiteur),
    path('test', views.test),
    path('logout', views.deconnexion),
    path('espace-agent', views.home),
    path('employe', views.employe),
    path('liste_des_visites', views.liste_des_visites),
    path('services', views.services),
    path('ajouter_employer', views.ajouter_employer),
    path('ajouter_service', views.ajouter_service),
    path('enregistrer-entree-sortie/<int:employe_id>', views.enregistrer_entree_sortie, name='enregistrer_entree_sortie'),

    path('employes', views.employe, name='employe'),
    #path('ajouter-employe', views.ajouter_employer, name='ajouter_employe'),
]

