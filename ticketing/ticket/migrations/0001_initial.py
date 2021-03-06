# Generated by Django 3.0 on 2020-07-14 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('base_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom du service')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cas', models.CharField(max_length=100, verbose_name='Description')),
                ('etat', models.CharField(choices=[('Créé', 'Créé'), ('En cours', 'En cours'), ('Résolu', 'Résolu')], max_length=10, verbose_name='Etat du ticket')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('contenu', models.CharField(max_length=512, verbose_name='Contenu du ticket')),
                ('commentaire', models.CharField(blank=True, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Client')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Service')),
            ],
        ),
    ]
