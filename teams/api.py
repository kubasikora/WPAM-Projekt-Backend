from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('contestants', views.ContestantListRESTView.as_view(), name='contestant_list'),
    path('contestants/<str:pk>', views.ContestantInstanceRESTView.as_view(), name='contestant_instance'),
    path('tournaments', views.TournamentListRESTView.as_view(), name='tournament_list'),
    path('tournaments/<str:pk>', views.TournamentInstanceRESTView.as_view(), name='tournament_instance'),
    path('matches/fixtures', views.FixtureListRESTView.as_view(), name='fixture_list'),
    path('matches/fixtures/<str:pk>', views.FixtureInstanceRESTView.as_view(), name='fixture_instance'),
    path('matches/results', views.ResultListRESTView.as_view(), name='result_list'),
    path('matches/results/<str:pk>', views.ResultInstanceRESTView.as_view(), name='result_instance')
]
