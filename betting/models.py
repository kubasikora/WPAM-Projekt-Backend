from django.db import models
from django.contrib.auth.models import User
from teams.models import Match, Tournament


class League(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=30)
    created = models.DateTimeField(verbose_name="Data dodania", auto_now_add=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name="Zawody")

    def __str__(self):
        return f'{self.name} in {self.tournament}'

    class Meta:
        ordering = ("-created",)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Użytkownik")
    points = models.PositiveIntegerField(verbose_name="Liczba punktów",default=0)
    joined = models.DateTimeField(verbose_name="Data dołączenia do ligi", auto_now_add=True)
    league = models.ForeignKey(League, verbose_name="Liga obstawiania", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} in {self.league}'

    class Meta:
        ordering = ("-points",)


class Bet(models.Model):
    date = models.DateTimeField(verbose_name="Data dodania", auto_now_add=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name="Mecz")
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name="Członek ligi")
    playerOnePrediction = models.PositiveIntegerField(verbose_name="Wynik zawodnika 1", default=0)
    playerTwoPrediction = models.PositiveIntegerField(verbose_name="Wynik zawodnika 2", default=0)

    def __str__(self):
        return f'{self.participant} on {self.match}'

    class Meta:
        ordering = ("-date",)
