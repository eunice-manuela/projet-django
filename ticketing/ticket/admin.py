from django.contrib import admin
from ticket.models import Service, Client, Ticket

admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Ticket)