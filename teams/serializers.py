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


class FixtureSnippetSerializer(serializers.ModelSerializer):
    playerOne = ContestantSnippetSerializer()
    playerTwo = ContestantSnippetSerializer()
    tournament = TournamentSnippetSerializer()

    class Meta:
        model = models.Match
        fields = ('id', 'playerOne', 'playerTwo', 'dateOfStart', 'sport', 'tournament')


class FixtureSerializer(serializers.ModelSerializer):
    playerOne = ContestantSerializer()
    playerTwo = ContestantSerializer()
    tournament = TournamentSnippetSerializer()

    class Meta:
        model= models.Match
        fields = '__all__'


class ResultSnippetSerializer(serializers.ModelSerializer):
    playerOne = ContestantSnippetSerializer()
    playerTwo = ContestantSnippetSerializer()
    tournament = TournamentSnippetSerializer()

    class Meta:
        model = models.Match
        fields = ('id', 'playerOne', 'playerOneResult', 'playerTwo', 'playerTwoResult', 'dateOfStart', 'sport', 'tournament')


class Result(models.Match):
    pass

class ResultSerializer(serializers.ModelSerializer):
    playerOne = ContestantSerializer()
    playerTwo = ContestantSerializer()
    tournament = TournamentSnippetSerializer()

    class Meta:
        model= Result
        fields = '__all__'
