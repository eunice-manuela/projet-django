from django.shortcuts import render, get_object_or_404
from .models import Terminaux_perdus
import requests


# Create your views here.

def Create(request):

    ticket = Terminaux_perdus(
        état = 'ouvert',
        client = request.GET.get('client'),
        identifiant_terminal = request.GET.get('terminal'),
        commentaires = ''
    )

    ticket.save()

    # envoie à tous les services
    url = 'url du service'
    r = requests.post(url,data=ticket)
    r.text()



def Edit(request, ticket_id):
    
    commentaires = request.GET.get('commentaire')
    ticket = get_object_or_404(Terminaux_perdus, pk=ticket_id)
    ticket.commentaires = commentaires
    if request.GET.get('état') == 'résolu':
        ticket.état = 'résolu'
    else:
        ticket.état = 'en cours'

    ticket.save()