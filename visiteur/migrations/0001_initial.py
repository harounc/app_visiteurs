# Generated by Django 4.2.13 on 2024-07-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_visiteur', models.TextField()),
                ('prenoms_visiteur', models.TextField()),
                ('type_piece', models.TextField()),
                ('numero_piece', models.TextField()),
            ],
        ),
    ]
