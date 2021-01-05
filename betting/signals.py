import uuid
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from betting.models import League, Participant, Bet

@receiver(pre_save, sender=League, dispatch_uid="create_league_key")
def createLeagueKey(sender,instance,**kwargs):
    instance.leagueKey = uuid.uuid4().hex[:6].upper()

@receiver(post_save, sender=Participant, dispatch_uid="create_past_matches")
def createPastMatches(sender, instance, created, **kwargs):
    if created:
        tournament = instance.league.tournament
        for match in tournament.matches.get_queryset():
            bet = Bet(match=match, participant=instance)
            bet.save()
