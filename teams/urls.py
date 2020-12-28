from django.urls import path
from teams import views
from django.contrib.auth.decorators import login_required

app_name = "teams"

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name="home"),

    path('matches', login_required(views.MatchListView.as_view()), name='match_list'),
    path('matches/new', login_required(views.MatchAddView.as_view()), name='match_add'),
    path('matches/<str:pk>', login_required(views.MatchUpdateView.as_view()), name='match_update'),
    
    path('tournaments', login_required(views.TournamentListView.as_view()), name='tournament_list'),
    path('tournaments/new', login_required(views.TournamentAddView.as_view()), name='tournament_add'),
    path('tournaments/<str:pk>', login_required(views.TournamentUpdateView.as_view()), name='tournament_update'),
    
    path('venues', login_required(views.VenueListView.as_view()), name='venue_list'),
    path('venues/new', login_required(views.VenueAddView.as_view()), name='venue_add'),
    path('venues/<str:pk>', login_required(views.VenueUpdateView.as_view()), name='venue_update'),
    
    path('countries', login_required(views.CountryListView.as_view()), name='country_list'),
    path('countries/new', login_required(views.CountryAddView.as_view()), name='country_add'),
    path('countries/<str:pk>', login_required(views.CountryUpdateView.as_view()), name='country_update'),
    
    path('contestants', login_required(views.ContestantListView.as_view()), name='contestant_list'),
    path('contestants/new', login_required(views.ContestantAddView.as_view()), name='contestant_add'),
    path('contestants/<str:pk>', login_required(views.ContestantUpdateView.as_view()), name='contestant_update')
]
