from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=20)
    addresse =models.CharField(max_length=20)

class User(models.Model):
    name=models.CharField(max_length=200)
    service=models.ForeignKey(Services, on_delete=models.CASCADE)

class responses(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    Author=models.ForeignKey(User, on_delete=models.CASCADE)
    Description=models.CharField(max_length=200)

class Tickets(models.Model):
    id=models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_création = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=250)
    priority=models.CharField(max_length=5)
    service= models.ForeignKey(Services, on_delete=models.CASCADE)
    

    def setManager(self,manager):
        self.manager=manager
    def setPriority(self, prior):
        self.priority=prior
    def setState(self, state):
        self.state=state
class Manager(models.Model):
    manager=models.ForeignKey(User, on_delete=models.CASCADE)
    ticket=models.ForeignKey(Tickets, on_delete=models.CASCADE)