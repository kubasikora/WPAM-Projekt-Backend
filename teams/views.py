from django.shortcuts import render
from django.views import generic 
from rest_framework import generics
from rest_framework.schemas.openapi import AutoSchema
from teams import models, serializers
from django.urls import reverse_lazy

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


"""Widok dodawania spotkania"""
class MatchAddView(generic.CreateView):
    model = models.Match
    template_name = "match/add.html"
    fields = "__all__"
    success_url = reverse_lazy("teams:match_list")


"""Widok listy wszystkich zawodów"""
class TournamentListView(generic.ListView):
    queryset = models.Tournament.objects.all()
    context_object_name = "tournaments"
    paginate_by = 50
    template_name = "tournament/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for tournament in context["object_list"]:
            tournament.numOfContestants = len(tournament.contestants.all())
        return context


"""Widok dodawania zawodów"""
class TournamentAddView(generic.CreateView):
    model = models.Tournament
    template_name = "tournament/add.html"
    fields = "__all__"
    success_url = reverse_lazy("teams:tournament_list")


"""Widok listy wszystkich krajów"""
class CountryListView(generic.ListView):
    queryset = models.Country.objects.all()
    context_object_name = "countries"
    paginate_by = 100
    template_name = "country/list.html"


"""Widok dodawania kraju"""
class CountryAddView(generic.CreateView):
    model = models.Country
    template_name = "country/add.html"
    fields = "__all__"
    success_url = reverse_lazy("teams:country_list")


"""Widok listy wszystkich obiektów sportowych"""
class VenueListView(generic.ListView):
    queryset = models.Venue.objects.all()
    context_object_name = "venues"
    paginate_by = 50
    template_name = "venue/list.html"


"""Widok dodawania obiektów sportowych"""
class VenueAddView(generic.CreateView):
    model = models.Venue
    template_name = "venue/add.html"
    fields = "__all__"
    success_url = reverse_lazy("teams:venue_list")


"""Widok listy wszystkich zawodników"""
class ContestantListView(generic.ListView):
    queryset = models.Contestant.objects.all()
    context_object_name = "contestants"
    paginate_by = 50
    template_name = "contestant/list.html"


"""Widok dodawania zawodników"""
class ContestantAddView(generic.CreateView):
    model = models.Contestant
    template_name = "contestant/add.html"
    fields = "__all__"
    success_url = reverse_lazy("teams:contestant_list")
