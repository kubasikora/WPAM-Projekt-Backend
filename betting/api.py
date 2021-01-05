from django.urls import path
from betting import views

app_name = "betting"

urlpatterns = [
    path('bets', views.BetListRESTView.as_view(), name='rest_bet_list'),
    path('post_bet', views.BetPostRESTView.as_view(), name='rest_post_bet'),
    path('bets/mine', views.UserBetsListRESTView.as_view(), name='rest_user_bets_list'),
    path('bets/mine/inLeague', views.UserBetsInLeagueListRESTView.as_view(), name='rest_user_bets_in_league_list'),

    path('leagues', views.LeagueListRESTView.as_view(), name='rest_league_list'),
    path('post_league', views.LeaguePostRESTView.as_view(), name='rest_post_league'),
    path('leagues/<str:pk>', views.LeagueListRESTView.as_view(),name='rest_league_instance'),
    path('leagues/<str:pk>/leaders', views.LeaderboardListRESTView.as_view(),name='rest_league_leaders_instance'),

    path('participants', views.ParticipantListRESTView.as_view(), name='rest_participants_list'),
    path('post_participant', views.ParticipantPostRESTView.as_view(), name='rest_post_participant'),
    path('participants/mine', views.ParticipantsOfUserListRESTView.as_view(), name='rest_participants_of_user_list')

]
