from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Visiteur

# Create your views here.
def index(request):
    return HttpResponse("BONJOUR")

def creer(request):
    if request.method == "GET":
        return render(request, "creer_visiteur.html")
    elif request.method == "POST":
        nom = request.POST.get("nom")
        prenoms = request.POST.get("prenoms")
        type_piece = request.POST.get("type_piece")
        numero_piece = request.POST.get("numero_piece")

        Visiteur.objects.create(nom_visiteur = nom, prenoms_visiteur = prenoms, type_piece = type_piece, numero_piece = numero_piece)
        # return HttpResponse("SUCCES")
        # return render(request, "creer_visiteur.html")
        return redirect("/creer")

