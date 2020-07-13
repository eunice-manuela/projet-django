from rest_framework import serializers
from ticket.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id',
                  'cas',
                  'etat',
                  'client',
                  'service',
                  'date_creation',
                  'commentaire')