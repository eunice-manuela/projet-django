from rest_framework import serializers
from ticket.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    service = serializers.StringRelatedField()
    class Meta:
        model = Ticket
        fields = ('id',
                  'cas',
                  'etat',
                  'client',
                  'service',
                  'date_creation',
                  'contenu',
                  'commentaire')

class TicketAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id',
                  'cas',
                  'etat',
                  'client',
                  'service',
                  'date_creation',
                  'contenu',
                  'commentaire')