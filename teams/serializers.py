from rest_framework import serializers
from teams import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ('name', 'code')


class VenueSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = models.Venue
        fields = '__all__'


class ContestantSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contestant
        fields = ('id', 'name')


class ContestantSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

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
        fields = ('id', 'playerOne', 'playerTwo', 'dateOfStart', 'sport')


class FixtureSerializer(serializers.ModelSerializer):
    playerOne = ContestantSerializer()
    playerTwo = ContestantSerializer()
    tournament = TournamentSnippetSerializer()
    venue = VenueSerializer()

    class Meta:
        model= models.Match
        fields = ('id', 'playerOne', 'playerTwo', 'dateOfStart', 'sport', 'tournament', 'venue')


class ResultSnippetSerializer(serializers.ModelSerializer):
    playerOne = ContestantSnippetSerializer()
    playerTwo = ContestantSnippetSerializer()
    tournament = TournamentSnippetSerializer()

    class Meta:
        model = models.Match
        fields = ('id', 'playerOne', 'playerOneResult', 'playerTwo', 'playerTwoResult', 'dateOfStart', 'sport', 'tournament')


class ResultSerializer(serializers.ModelSerializer):
    playerOne = ContestantSerializer()
    playerTwo = ContestantSerializer()
    tournament = TournamentSnippetSerializer()
    venue = VenueSerializer()

    class Meta:
        model= models.Match
        fields = '__all__'
