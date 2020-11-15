from django.urls import path
from teams import views

app_name = "teams"

urlpatterns = [
    path('', views.ContestantListRESTView.as_view(), name='contestant_list'),
    path('<str:pk>', views.ContestantInstanceRESTView.as_view(), name='contestant_instance')
]