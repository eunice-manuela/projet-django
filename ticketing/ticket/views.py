from django.shortcuts import render
from django.http.response import JsonResponse
from django.db.models import Q

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import random

from ticket.models import Client, Service, Ticket
from ticket.serializers import TicketSerializer, TicketAddSerializer

@api_view(['GET', 'POST'])
def ticket_list(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()

        cas = request.GET.get('cas', None)
        etat = request.GET.get('etat', None)
        if cas is not None:
            tickets = tickets.filter(cas__icontains=cas)
        if etat is not None:
            tickets = tickets.filter(etat=etat)

        tickets_serializer = TicketSerializer(tickets, many=True)
        return JsonResponse(tickets_serializer.data, safe=False)

    elif request.method == 'POST':
        ticket_data = JSONParser().parse(request)
        ticket_serializer = TicketAddSerializer(data=ticket_data)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            return JsonResponse(ticket_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def ticket_detail(request, pk):
    # find ticket by pk (id)
    try:
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return JsonResponse({'message': 'The ticket does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT ticket
    if request.method == 'GET':
        ticket_serializer = TicketSerializer(ticket)
        return JsonResponse(ticket_serializer.data)

    elif request.method == 'PUT':
        ticket_data = JSONParser().parse(request)
        ticket_serializer = TicketSerializer(ticket, data=ticket_data)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            return JsonResponse(ticket_serializer.data)
        return JsonResponse(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client(request):
    return JsonResponse(random.choices(list(Client.objects.values_list('pk', flat=True)))[0], safe=False)

@api_view(['GET'])
def service(request):
    return JsonResponse(random.choices(list(Service.objects.values_list('pk', flat=True)))[0], safe=False)