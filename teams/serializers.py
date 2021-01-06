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
        fields = ('id', 'name','sport')


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

class MatchStatisticsSerializer(serializers.ModelSerializer):
    playerOne = ContestantSerializer()
    playerTwo = ContestantSerializer()
    playerOneForm = serializers.SerializerMethodField('get_player_one_form')
    playerTwoForm = serializers.SerializerMethodField('get_player_two_form')
    venue = VenueSerializer()

    def get_player_form(self, match, player):
        queryset = models.Match.objects.filter(dateOfStart__lt=match.dateOfStart, finished=True)
        result = queryset.filter(playerOne=player) | queryset.filter(playerTwo=player)
        data = result.order_by("-dateOfStart")[:5]
        form = []
        for match in data:
            if match.playerOne == player:
                if match.playerOneResult > match.playerTwoResult:
                    form.append(f"W vs {match.playerTwo}")
                    continue
                if match.playerOneResult == match.playerTwoResult:
                    form.append(f"D vs {match.playerTwo}")
                    continue
                if match.playerOneResult < match.playerTwoResult:
                    form.append(f"L vs {match.playerTwo}")
                    continue
            if match.playerTwo == player:
                if match.playerOneResult > match.playerTwoResult:
                    form.append(f"L vs {match.playerOne}")
                    continue
                if match.playerOneResult == match.playerTwoResult:
                    form.append(f"D vs {match.playerOne}")
                    continue
                if match.playerOneResult < match.playerTwoResult:
                    form.append(f"W vs {match.playerOne}")
                    continue
        return form

    def get_player_one_form(self, obj):
        return self.get_player_form(obj, obj.playerOne)

    def get_player_two_form(self, obj):
        return self.get_player_form(obj, obj.playerTwo)

    class Meta:
        model = models.Match
        fields = ('id', 'playerOne', 'playerOneResult', 'playerTwo', 'playerTwoResult', 'dateOfStart', 'finished', 'playerOneForm', 'playerTwoForm', 'venue')

