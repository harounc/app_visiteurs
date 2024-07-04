from django.db import models

# Model Visiteur
class Visiteur(models.Model):
    # <nom_du_champ> = models.<Type>

    id = models.BigAutoField()
    nom_visiteur = models.TextField()
    prenoms_visiteur = models.TextField()
    type_piece = models.TextField()
    numero_piece = models.TextField()


    """
    1. On crée le model

    2. On crée les migrations -> python manage.py makemigrations
        Une migration est un fichier qui transforme du code python en SQL 

    3. On applique les migrations -> python manage.py migrate
        Cela revient à dire à Django de d'exécuter le code SQL généré
    """