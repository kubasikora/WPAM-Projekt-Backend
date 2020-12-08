from rest_framework import serializers
from betting import models
from django.contrib.auth.models import User
from teams.serializers import ResultSerializer, TournamentSnippetSerializer


class BetSerializer(serializers.ModelSerializer):
    match = ResultSerializer()

    class Meta:
        model = models.Bet
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class ParticipantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Participant
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    tournament = TournamentSnippetSerializer()
    contestants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = models.League
        fields = '__all__'

