from django.shortcuts import render
from .models import Tickets
from django.shortcuts import get_object_or_404
import requests


# Create your views here.

def Create(request):

    ticket = Tickets(
        cas=request.GET.get('cas'),
        état = 'ouvert',
        client = request.GET.get('client'),
        service = request.GET.get('service'),
        commentaires = ''
    )

    ticket.save()

    # ecrire l'envoie de la requête
    url = 'url du service'
    r = requests.post(url,data=ticket)
    r.text()



def Edit(request, ticket_id):
    
    commentaires = request.GET.get('commentaire')
    ticket = get_object_or_404(Tickets, pk=ticket_id)
    ticket.commentaires = commentaires

    ticket.save()
    
