
from rest_framework import generics
from rest_framework.schemas.openapi import AutoSchema
from betting import models, serializers


# rest endpoint views
"""Widok listy wszystkich dostępnych zakładów"""
class BetListRESTView(generics.ListAPIView):
    queryset = models.Bet.objects.all()
    serializer_class = serializers.BetSerializer
    schema = AutoSchema(operation_id_base='TBD', tags=['betting'])


class BetPlaceRESTView(generics.UpdateAPIView):
    queryset = models.Bet.objects.all()
    serializer_class = serializers.BetShortSerializer
    schema = AutoSchema(operation_id_base='place_bet', tags=['betting'])


"""Widok listy wszystkich dostępnych zakładów konkretnego użytkownika"""
class UserBetsListRESTView(generics.ListAPIView):
    serializer_class = serializers.BetSerializer
    schema = AutoSchema(operation_id_base='user_bets', tags=['betting'])

    def get_queryset(self):
        return models.Bet.objects.filter(participant__user=self.request.user)


class UserBetsInLeagueListRESTView(generics.ListAPIView):
    serializer_class = serializers.BetSerializer
    schema = AutoSchema(operation_id_base='user_bets_in_league', tags=['betting'])

    filter_params = ('league',)

    def get_queryset(self):
        leagueId = self.request.query_params.get('league', None)
        return models.Bet.objects.filter(participant__user=self.request.user,
                                         participant__league=leagueId)


class LeagueListRESTView(generics.ListAPIView):
    queryset = models.League.objects.all()
    serializer_class = serializers.LeagueSerializer
    schema = AutoSchema(tags=['betting'])


class LeaderboardListRESTView(generics.RetrieveAPIView):
    serializer_class = serializers.LeaderboardSerializer
    schema = AutoSchema(operation_id_base='leaders',tags=['betting'])

    def get_queryset(self):
        leagueid = self.kwargs["pk"]
        return models.League.objects.filter(id=leagueid)

class LeaguePostRESTView(generics.CreateAPIView):
    queryset = models.League.objects.all()
    serializer_class = serializers.LeagueShortSerializer
    schema = AutoSchema(operation_id_base='post_league', tags=['betting'])


class ParticipantListRESTView(generics.ListAPIView):
    queryset = models.Participant.objects.all()
    serializer_class = serializers.ParticipantSerializer
    schema = AutoSchema(tags=['betting'])


class ParticipantPostRESTView(generics.CreateAPIView):
    serializer_class = serializers.ParticipantOnlyPointsSerializer
    schema = AutoSchema(operation_id_base='post_participant', tags=['betting'])

    def perform_create(self, serializer):
        leagueKey = self.kwargs["leagueKey"]
        serializer.save(league=models.League.objects.filter(leagueKey=leagueKey).first(),
                        user=self.request.user)


class ParticipantsOfUserListRESTView(generics.ListAPIView):
    serializer_class = serializers.ParticipantSerializer
    schema = AutoSchema(operation_id_base='user_participants', tags=['betting'])

    def get_queryset(self):
        return models.Participant.objects.filter(user=self.request.user)


class ParticipantOfUserForLeagueListRESTView(generics.ListAPIView):
    serializer_class = serializers.ParticipantSerializer
    schema = AutoSchema(operation_id_base='user_participants', tags=['betting'])
    filter_params = ('league',)

    def get_queryset(self):
        leagueId = self.request.query_params.get('league', None)
        return models.Participant.objects.filter(user=self.request.user,
                                                 league=leagueId)
