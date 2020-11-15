from django.shortcuts import render
from rest_framework import generics
from teams import models, serializers

class ContestantListRESTView(generics.ListAPIView):
    queryset = models.Contestant.objects.all()
    serializer_class = serializers.ContestantSnippetSerializer

class ContestantInstanceRESTView(generics.RetrieveAPIView):
    queryset = models.Contestant.objects.all()
    serializer_class = serializers.ContestantSerializer
