from django.shortcuts import render
from django.views import generic 
from rest_framework import generics
from rest_framework.schemas.openapi import AutoSchema
from teams import models, serializers

# rest endpoint views

"""Widok listy wszystkich dostępnych zawodników/drużyn"""
class ContestantListRESTView(generics.ListAPIView):
    queryset = models.Contestant.objects.all()
    serializer_class = serializers.ContestantSnippetSerializer
    schema = AutoSchema(tags=['teams'])


"""Widok szczegółowy danego zawodnika/drużyny"""
class ContestantInstanceRESTView(generics.RetrieveAPIView):
    queryset = models.Contestant.objects.all()
    serializer_class = serializers.ContestantSerializer
    schema = AutoSchema(tags=['teams'])


"""Widok listy wszystkich dostępnych zawodów"""
class TournamentListRESTView(generics.ListAPIView):
    queryset = models.Tournament.objects.all()
    serializer_class = serializers.TournamentSnippetSerializer
    schema = AutoSchema(tags=['teams'])


"""Widok szczegółowy danych zawodów"""
class TournamentInstanceRESTView(generics.RetrieveAPIView):
    queryset = models.Tournament.objects.all()
    serializer_class = serializers.TournamentSerializer
    schema = AutoSchema(tags=['teams'])


"""Widok listy wszystkich spotkań/meczów które jeszcze się nie zakończyły"""
class FixtureListRESTView(generics.ListAPIView):
    queryset = models.Match.objects.filter(finished=False).all()
    serializer_class = serializers.FixtureSnippetSerializer
    schema = AutoSchema(operation_id_base='fixture', tags=['teams'])


"""Widok szczegółowy spotkania/meczu który jeszcze się nie zaczął"""
class FixtureInstanceRESTView(generics.RetrieveAPIView):
    queryset = models.Match.objects.filter(finished=False).all()
    serializer_class = serializers.FixtureSerializer
    schema = AutoSchema(operation_id_base='fixture', tags=['teams'])


"""Widok listy wszystkich spotkań/meczów które już sie zakończyły"""
class ResultListRESTView(generics.ListAPIView):
    queryset = models.Match.objects.filter(finished=True).all()
    serializer_class = serializers.ResultSnippetSerializer
    schema = AutoSchema(operation_id_base='result', tags=['teams'])


"""Widok szczegółowy spotkania/meczu który już się zakończył"""
class ResultInstanceRESTView(generics.RetrieveAPIView):
    queryset = models.Match.objects.filter(finished=True).all()
    serializer_class = serializers.ResultSerializer
    schema = AutoSchema(operation_id_base='result', tags=['teams'])
    
# template-based views

"""Widok startowy CMSa aplikacji teams"""
class HomeView(generic.TemplateView):
    template_name = "teams_home.html"


"""Widok listy wszystkich spotkań"""
class MatchListView(generic.ListView):
    queryset = models.Match.objects.all()
    context_object_name = "matches"
    paginate_by = 50
    template_name = "match/list.html"