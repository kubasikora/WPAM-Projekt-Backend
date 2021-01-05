from django.db.models.signals import post_save
from django.dispatch import receiver

from teams.models import Match, Tournament
from betting.models import Bet, Participant

def pointsToAdd(match, bet):
    if match.playerOneResult == bet.playerOnePrediction and match.playerTwoResult == bet.playerTwoPrediction:
        return 3
    if match.playerOneResult > match.playerTwoResult and bet.playerOnePrediction > bet.playerTwoPrediction:
        return 1
    if match.playerOneResult < match.playerTwoResult and bet.playerOnePrediction < bet.playerTwoPrediction:
        return 1
    if match.playerOneResult == match.playerTwoResult and bet.playerOnePrediction == bet.playerTwoPrediction:
        return 1
    return 0


@receiver(post_save, sender=Match, dispatch_uid="create_bets")
def createBetsForAllParticipants(sender, instance, created, **kwargs):
    if created:
        """
        New match was created, therefore we have to create new bet object
        for all participants that might be interested
        """
        for league in instance.tournament.betting_leagues.get_queryset():
            for participant in league.participants.get_queryset():
                bet = Bet(match=instance, participant=participant)
                bet.save()
    else:
        """
        Already existing match was updated, so we have to update scores
        of all participants that put bet on this match
        """
        if instance.finished:
            for bet in instance.bets.get_queryset():
                if not bet.cashout and bet.valid:
                    bet.participant.points += pointsToAdd(instance, bet)
                    bet.participant.save()

                    bet.cashout = True
                    bet.save()
