from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('matches', views.MatchListView.as_view(), name='match_list'),
]
