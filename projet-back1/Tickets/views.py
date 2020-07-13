from django.shortcuts import render, get_object_or_404
from .models import Tickets
import requests
from django.http import JsonResponse


# Create your views here.

def Create(request):

    ticket = Tickets(
        title=request.get('title'),
        auteur=request.get('auteur_id'),
        details=request.get('details'),
        service = request.GET.get('service'),
    )
    ticket.setState('opened')
    ticket.save()
    data={'status':"success"}
    JsonResponse(data)

def home(request):
    return JsonResponse({'oooo':'lllll'})
    
def getTickets(request):
    tickets = Tickets.objects.all()[:50]
    data={'status':"success",
    'items':tickets}
    JsonResponse(data)
def delete(request):
    id=request._get('ticket_id')
    ticket=Tickets.get(id=id)
    ticket.delete()
    data={'status':'success'}
    JsonResponse(data)


#def response_tiket(request):
#   editType=request.get('type')
#  if editType = 'setPriority':
#     edittype
 

def Edit(request):

    commentaires = request.GET.get('commentaire')
    ticket = get_object_or_404(Tickets, pk=ticket_id)
    ticket.commentaires = commentaires
    if request.GET.get('état') == 'résolu':
        ticket.état = 'résolu'
    else:
        ticket.état = 'en cours'

    ticket.save()
    
