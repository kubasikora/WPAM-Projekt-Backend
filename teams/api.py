from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('contestants', views.ContestantListRESTView.as_view(), name='rest_contestant_list'),
    path('contestants/<str:pk>', views.ContestantInstanceRESTView.as_view(), name='rest_contestant_instance'),
    path('tournaments', views.TournamentListRESTView.as_view(), name='rest_tournament_list'),
    path('tournaments/active', views.ActiveTournamentListRESTView.as_view(), name='rest_active_tournament_list'),
    path('tournaments/<str:pk>', views.TournamentInstanceRESTView.as_view(), name='rest_tournament_instance'),
    path('matches/fixtures', views.FixtureListRESTView.as_view(), name='rest_fixture_list'),
    path('matches/fixtures/<str:pk>', views.FixtureInstanceRESTView.as_view(), name='fixture_instance'),
    path('matches/results', views.ResultListRESTView.as_view(), name='rest_result_list'),
    path('matches/results/<str:pk>', views.ResultInstanceRESTView.as_view(), name='rest_result_instance')
]
