from rest_framework import serializers
from teams import models

class ContestantSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contestant
        fields = ('id', 'name')


class ContestantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contestant
        fields = '__all__'


class TournamentSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tournament
        fields = ('id', 'name', 'sport')


class TournamentSerializer(serializers.ModelSerializer):
    contestants = ContestantSnippetSerializer(many=True, read_only=True)

    class Meta:
        model = models.Tournament
        fields = '__all__'
