from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Visiteur


# Create your views here.
def index(request):
    context = {}
    print(request.user)
    if request.user.is_authenticated:
        return redirect("/espace-agent")

    if request.method == "POST":
        email = request.POST.get("email")
        if not email:
            context['erreur'] = 'email est obligatoire'

        password = request.POST.get("password")
        if not password:
            context['erreur'] = 'password est obligatoire'

        user = authenticate(username = email, password = password)
        if user:
            context['succes'] = 'vous êtes connectez'
            login(request, user)
            return redirect("/")
        else:
            context['erreur'] = 'informations incorrects'

    return render(request, "login.html", context)

def home(request):
    if not request.user.is_authenticated:
        return redirect("/")
    return render(request, "espace-agent.html")

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

def deconnexion(request):
    logout(request)
    return redirect("/")
def test(request):
    tous = Visiteur.objects.all()
    # print("\n", tous)
    # print("\n", tous[0], type(tous[0]))
    first = tous[0]
    # print("\n", first, type(first))

    # creation : OPTION 1 : créer directement l'objet dans la DB
    """
    harouna = Visiteur.objects.create(
        nom_visiteur="COUL",
        prenoms_visiteur="Har",
        type_piece="CNI",
        numero_piece="CNI00118485418")
    print(harouna.id)
    
    """

    # creation : OPTION 2 : elle se fait en 2 étapes (on crée d'abord l'objet dans python et ensuite le stocke dans la DB)

    # Etape 1 : création de l'objet dans python
    """
    harouna = Visiteur(
        nom_visiteur="COUL",
        prenoms_visiteur="Har",
        type_piece="CNI",
        numero_piece="CNI00118485418")
    print(harouna)
    print("id :",harouna.id)
    """
    # Etape 2 : création de l'objet dans la DB
    """
    harouna.save()
    print("new id :", harouna.id)
    """

    # Recuperer un visiteur
    """
    try:
        visiteur = Visiteur.objects.get(id=9)
    except:
        return HttpResponse("Visiteur non trouvé, ou n'existe pas")

    print(visiteur)    
    
    """

    # Filtrer les recherches

    filtre = Visiteur.objects.filter(nom_visiteur = "COUIBALY", prenoms_visiteur = "Harouna").all()
    print("\n", filtre)
    for visiteur in tous:
        print(visiteur.nom_visiteur, visiteur.prenoms_visiteur)


    return render(request, "test.html", context={'liste_visiteurs':tous, 'titre':'django pour toujours'})