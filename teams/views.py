from django.shortcuts import render
from rest_framework import generics
from teams import models, serializers

class TeamListRESTView(generics.ListAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSnippetSerializer

class TeamInstanceRESTView(generics.RetrieveAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
