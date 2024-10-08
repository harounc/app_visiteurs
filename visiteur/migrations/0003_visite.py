# Generated by Django 4.2.13 on 2024-07-06 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visiteur', '0002_visiteur_numero_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif_visite', models.TextField()),
                ('heure_entree', models.DateTimeField()),
                ('heure_sortie', models.DateTimeField()),
                ('id_visiteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visiteur.visiteur')),
            ],
        ),
    ]
