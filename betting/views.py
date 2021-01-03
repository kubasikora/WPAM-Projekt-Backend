from rest_framework import generics
from rest_framework.schemas.openapi import AutoSchema
from betting import models, serializers


# rest endpoint views

"""Widok listy wszystkich dostępnych zakładów"""
class BetListRESTView(generics.ListAPIView):
    queryset = models.Bet.objects.all()
    serializer_class = serializers.BetSerializer
    schema = AutoSchema(operation_id_base='TBD', tags=['betting'])


"""Widok listy wszystkich dostępnych zakładów konkretnego użytkownika"""
class UserBetsListRESTView(generics.ListAPIView):
    serializer_class = serializers.BetSerializer
    schema = AutoSchema(operation_id_base='user_bets', tags=['betting'])

    """ Żeby filtrować wynik po użytkowniku trzeba nadpisać funkcję get_queryset
        i tam można działać cuda
    """
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


class ParticipantListRESTView(generics.ListAPIView):
    queryset = models.Participant.objects.all()
    serializer_class = serializers.ParticipantSerializer
    schema = AutoSchema(tags=['betting'])


class ParticipantsOfUserListRESTView(generics.ListAPIView):
    serializer_class = serializers.ParticipantSerializer
    schema = AutoSchema(operation_id_base='user_participants', tags=['betting'])

    def get_queryset(self):
        print(self.request.user)
        return models.Participant.objects.filter(user=self.request.user)
