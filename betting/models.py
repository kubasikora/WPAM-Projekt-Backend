from django.db import models
from django.contrib.auth.models import User
from teams.models import Match

class Bet(models.Model):
    date = models.DateTimeField(verbose_name="Data dodania", auto_now_add=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name="Mecz")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")



    def __str__(self):
        return f'{self.user} on {self.match}'

    class Meta:
        ordering = ("-date",)


