from rest_framework import serializers
from betting import models
from django.contrib.auth.models import User
from teams.serializers import ResultSerializer, TournamentSnippetSerializer


class BetSerializer(serializers.ModelSerializer):
    match = ResultSerializer()

    class Meta:
        model = models.Bet
        fields = '__all__'

class BetShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bet
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class LeagueSerializer(serializers.ModelSerializer):
    tournament = TournamentSnippetSerializer()
    class Meta:
        model = models.League
        fields = '__all__'


class LeagueShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.League
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    league = LeagueSerializer()
    class Meta:
        model = models.Participant
        fields = '__all__'


class ParticipantShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Participant
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True)
    class Meta:
        model = models.League
        fields = ('participants',)

