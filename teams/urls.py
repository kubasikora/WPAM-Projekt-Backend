from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('matches', views.MatchListView.as_view(), name='match_list'),
    path('matches/new', views.MatchAddView.as_view(), name='match_add'),
    path('tournaments', views.TournamentListView.as_view(), name='tournament_list'),
    path('venues', views.VenueListView.as_view(), name='venue_list'),
    path('countries', views.CountryListView.as_view(), name='country_list'),
    path('contestants', views.ContestantListView.as_view(), name='contestant_list')
]
