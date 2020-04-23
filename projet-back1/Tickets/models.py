from django.db import models

# Create your models here.

class Tickets(models.Model):
    cas = models.CharField(max_length=100)
    état = models.CharField(max_length=10)
    client = models.CharField(max_length=36)
    service = models.CharField(max_length=25)
    date_création = models.DateTimeField(auto_now_add=True)
    commentaires = models.CharField(max_length=250)