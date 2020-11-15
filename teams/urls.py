from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('contestants', views.ContestantListRESTView.as_view(), name='contestant_list'),
    path('contestants/<str:pk>', views.ContestantInstanceRESTView.as_view(), name='contestant_instance'),
    path('tournaments', views.TournamentListRESTView.as_view(), name='tournament_list'),
    path('tournaments/<str:pk>', views.TournamentInstanceRESTView.as_view(), name='tournament_instance')
]