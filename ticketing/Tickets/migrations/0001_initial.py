# Generated by Django 3.0.3 on 2020-07-13 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('addresse', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.Services')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=10)),
                ('date_création', models.DateTimeField(auto_now_add=True)),
                ('details', models.CharField(max_length=250)),
                ('priority', models.CharField(max_length=5)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.User')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.Services')),
            ],
        ),
        migrations.CreateModel(
            name='responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Description', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.User')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.User')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.Tickets')),
            ],
        ),
    ]
