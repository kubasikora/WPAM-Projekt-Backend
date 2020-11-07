from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('', views.TeamListRESTView.as_view(), name='team_list'),
    path('<str:pk>', views.TeamInstanceRESTView.as_view(), name='team_instance')
]