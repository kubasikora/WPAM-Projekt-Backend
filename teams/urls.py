from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

    path('matches', views.MatchListView.as_view(), name='match_list'),
    path('matches/new', views.MatchAddView.as_view(), name='match_add'),
    
    path('tournaments', views.TournamentListView.as_view(), name='tournament_list'),
    path('tournaments/new', views.TournamentAddView.as_view(), name='tournament_add'),
    
    path('venues', views.VenueListView.as_view(), name='venue_list'),
    path('venues/new', views.VenueAddView.as_view(), name='venue_add'),
    
    path('countries', views.CountryListView.as_view(), name='country_list'),
    path('countries/new', views.CountryAddView.as_view(), name='country_add'),
    
    path('contestants', views.ContestantListView.as_view(), name='contestant_list'),
    path('contestants/new', views.ContestantAddView.as_view(), name='contestant_add')
]
