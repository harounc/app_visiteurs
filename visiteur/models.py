from django.db import models

# Model Service
class Service(models.Model):
    nom_service = models.TextField()


# Model Visiteur
class Visiteur(models.Model):
    # <nom_du_champ> = models.<Type>

    #id = models.BigAutoField()
    nom_visiteur = models.TextField()
    prenoms_visiteur = models.TextField()
    type_piece = models.TextField()
    numero_piece = models.TextField()
    numero_test = models.TextField()
    role_visiteur = models.TextField(null = True)
    mon_service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)


    """
    1. On crée le model

    2. On crée les migrations -> python manage.py makemigrations
        Une migration est un fichier qui transforme du code python en SQL 

    3. On applique les migrations -> python manage.py migrate
        Cela revient à dire à Django de d'exécuter le code SQL généré
    """

class Visite(models.Model):
    motif_visite = models.TextField()
    heure_entree = models.DateTimeField()

    # On rajoute "null = True" pour rendre le champ optionnel dans la DB 
    heure_sortie = models.DateTimeField(null = True)
    visiteur = models.ForeignKey(Visiteur, on_delete=models.CASCADE)
    service_visite = models.ForeignKey(Service, on_delete=models.CASCADE, null = True)
