from rest_framework import generics
from rest_framework.schemas.openapi import AutoSchema
from betting import models, serializers


# rest endpoint views

"""Widok listy wszystkich dostępnych zawodników/drużyn"""
class BetListRESTView(generics.ListAPIView):
    queryset = models.Bet.objects.all()
    serializer_class = serializers.BetSerializer
    schema = AutoSchema(operation_id_base='TBD', tags=['betting'])


class LeagueListRESTView(generics.ListAPIView):
    queryset = models.League.objects.all()
    serializer_class = serializers.LeagueSerializer
    schema = AutoSchema(tags=['betting'])


class ParticipantListRESTView(generics.ListAPIView):
    queryset = models.Participant.objects.all()
    serializer_class = serializers.ParticipantSerializer
    schema = AutoSchema(tags=['betting'])
