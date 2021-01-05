import uuid

from django.db.models.signals import pre_save
from django.dispatch import receiver

from betting.models import League

@receiver(pre_save, sender=League, dispatch_uid="create_league_key")
def createLeagueKey(sender,instance,**kwargs):
    instance.leagueKey = uuid.uuid4().hex[:6].upper()
