from django.db.models.signals import post_save
from django.dispatch import receiver

from teams.models import Match, Tournament
from betting.models import Bet, Participant

@receiver(post_save, sender=Match, dispatch_uid="create_bets")
def createBetsForAllParticipants(sender, instance, created, **kwargs):
    if created:
        for league in instance.tournament.betting_leagues.get_queryset():
            for participant in league.participants.get_queryset():
                bet = Bet(match=instance, participant=participant)
                bet.save()
