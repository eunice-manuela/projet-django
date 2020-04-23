from django.db import models

# Create your models here.

class Terminaux_perdus(models.Model):
    client = models.CharField(max_length=36)
    identifiant_terminal = models.CharField(max_length=50)
    date_création = models.DateTimeField(auto_now_add=True)
