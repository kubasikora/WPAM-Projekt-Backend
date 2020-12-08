from django.urls import path
from betting import views

app_name = "betting"

urlpatterns = [
    path('bets', views.BetListRESTView.as_view(), name='rest_bet_list'),
    path('leagues', views.LeagueListRESTView.as_view(), name='rest_league_list'),
    path('participants', views.ParticipantListRESTView.as_view(), name='rest_participants_list')
]
