from django.contrib.auth import authenticate, login, logout
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Visiteur, Visite, Service
from django.db.models import Q

"""
TODO:
    - Nombre total de visites ce mois
    - Prendre en compte le service que l'utilisateur va visiter et la personne 
        - Ajouter les champs nécessaires dans le Model Visite
        - Modifier le formulaire d'ajout pour correcpondre aux nouveaux champ ajoutés
    Next
    - Nombre de visites par service / periode
    - Ajouter la prise en compte des utilsateurs internes

"""

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

def home(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("/")
    
    contenu_message = request.GET.get("message")
    visites = Visite.objects.order_by("-id").all()

    # today_minuit = datetime.datetime.now()
    # today_minuit.replace(hour=0, minute=0, second=0, microsecond=0)

    # today_23h = datetime.datetime.now()
    # today_23h.replace(hour=23, minute=59, second=59)

    # nombre_visiteur_today = Visite.objects.filter(
    #     # heure_entree__gt = today_minuit,
    #     # heure_entree__lt = today_23h,
    # ).count()

    today = datetime.date.today()

    indice_today_dans_la_semaine = today.weekday()
    lundi = today - datetime.timedelta(days = indice_today_dans_la_semaine)
    dimanche = lundi + datetime.timedelta(days = 6)

    nombre_visiteur_today = Visite.objects.filter(
        heure_entree__date = today
    ).count()

    nombre_visiteur_semaine = Visite.objects.filter(
        heure_entree__gt = lundi,
        heure_entree__lt = dimanche,
    ).count()

    return render(
        request, 
        "espace-agent.html", 
        { 
            'success_message': contenu_message,
            'liste_visites': visites,
            'nombre_visiteur_today': nombre_visiteur_today,
            'nombre_visiteur_semaine': nombre_visiteur_semaine,
        }
    )



def creer_nouveau_visiteur(request):
    if request.method == "GET":
        return render(request, "creer_visiteur.html")
    elif request.method == "POST":
        nom = request.POST.get("nom")
        prenoms = request.POST.get("prenoms")
        type_piece = request.POST.get("type_piece")
        numero_piece = request.POST.get("numero_piece")
        motif = request.POST.get("motif")

        visiteur = Visiteur.objects.create(nom_visiteur = nom, prenoms_visiteur = prenoms, type_piece = type_piece, numero_piece = numero_piece)
        
        Visite.objects.create(
            motif_visite = motif,
            heure_entree = datetime.datetime.now(),
            visiteur = visiteur
        )
        # return HttpResponse("SUCCES")
        # return render(request, "creer_visiteur.html")
        return redirect("/espace-agent?message=Visiteur créé avec success")
    
def deconnexion(request):
    logout(request)
    return redirect("/")

#def employe(request):
#    context = {}
#    return render(request, "employe.html", context)

"""
def employe(request):
    employes = Visiteur.objects.filter(role_visiteur="employer").select_related('mon_service')
    context = {
        'employes': employes
    }
    return render(request, "employe.html", context)
"""

def employe(request):
    query = request.GET.get('search', '')  # Récupération de la requête de recherche
    employes = Visiteur.objects.filter(role_visiteur="employer")

    # Si une recherche est effectuée
    if query:
        employes = employes.filter(
            Q(nom_visiteur__icontains=query) | Q(prenoms_visiteur__icontains=query)
        )

    # Nombre total d'employés
    nombre_total_employes = Visiteur.objects.filter(role_visiteur="employer").count()

    context = {
        'employes': employes,
        'search_query': query,  # Pour garder la requête de recherche dans le champ
        'nombre_total_employes': nombre_total_employes,  # Nombre total d'employés
    }
    return render(request, "employe.html", context)


"""
def liste_des_visites(request):
    context = {}
    return render(request, "liste_des_visites.html", context)
"""
def liste_des_visites(request):
    contenu_message = request.GET.get("message")
    visites = Visite.objects.order_by("-id").all()

        # today_minuit = datetime.datetime.now()
        # today_minuit.replace(hour=0, minute=0, second=0, microsecond=0)

        # today_23h = datetime.datetime.now()
        # today_23h.replace(hour=23, minute=59, second=59)

        # nombre_visiteur_today = Visite.objects.filter(
        #     # heure_entree__gt = today_minuit,
        #     # heure_entree__lt = today_23h,
        # ).count()

    today = datetime.date.today()

    indice_today_dans_la_semaine = today.weekday()
    lundi = today - datetime.timedelta(days = indice_today_dans_la_semaine)
    dimanche = lundi + datetime.timedelta(days = 6)

    nombre_visiteur_today = Visite.objects.filter(
        heure_entree__date = today
    ).count()

    nombre_visiteur_semaine = Visite.objects.filter(
        heure_entree__gt = lundi,
        heure_entree__lt = dimanche,
    ).count()

    return render(
        request,
        "liste_des_visites.html",
        {
            'success_message': contenu_message,
            'liste_visites': visites,
            'nombre_visiteur_today': nombre_visiteur_today,
            'nombre_visiteur_semaine': nombre_visiteur_semaine,
        }
    )



#def services(request):
#    context = {}
#    return render(request, "services.html", context)

def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, "services.html", context)


def ajouter_employer(request):
    if request.method == "GET":
        services = Service.objects.all()  # Récupère tous les services
        return render(request, "ajouter_employer.html", {'services': services})
    elif request.method == "POST":
        nom = request.POST.get("nom")
        prenoms = request.POST.get("prenoms")
        type_piece = request.POST.get("type_piece")
        numero_piece = request.POST.get("numero_piece")
        #service = request.POST.get("service")
        service_id = request.POST.get("service")

        # Assurez-vous de récupérer l'instance du Service
        service = get_object_or_404(Service, id=service_id)

        visiteur = Visiteur.objects.create(nom_visiteur=nom, prenoms_visiteur=prenoms, type_piece=type_piece,
                                           numero_piece=numero_piece, mon_service=service, role_visiteur="employer")
        return redirect("/ajouter_employer?message=employer créé avec success")

'''
        Visite.objects.create(
            motif_visite=motif,
            heure_entree=datetime.datetime.now(),
            visiteur=visiteur
        )
        # return HttpResponse("SUCCES")
        # return render(request, "creer_visiteur.html")
'''


def ajouter_service(request):
    if request.method == "GET":
        return render(request, "ajouter_service.html")
    elif request.method == "POST":
        service = request.POST.get("nom_service")

        service = Service.objects.create(nom_service=service)
        return redirect("/ajouter_service?message=service créé avec success")


def enregistrer_entree_sortie(request, employe_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        employe = Visiteur.objects.get(id=employe_id)

        if action == "ENTREE":
            # Créer une nouvelle entrée pour l'employé
            Visite.objects.create(
                visiteur=employe,
                motif_visite='ENTREE',  # Mettre un motif pertinent ici
                heure_entree=datetime.datetime.now()
            )
        elif action == "SORTIE":
            # Marquer la sortie pour cet employé
            # Par exemple, ajouter l'heure de sortie à la dernière visite sans heure de sortie
            derniere_visite = Visite.objects.filter(visiteur=employe).order_by('-heure_entree').first()
            if derniere_visite and not derniere_visite.heure_sortie:
                derniere_visite.heure_sortie = datetime.datetime.now()
                derniere_visite.save()

        # Redirection vers la page des employés avec un message de succès
        return redirect(f"/employes?message={action} enregistrée avec succès")


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