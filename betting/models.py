from django.db import models
from django.contrib.auth.models import User
from teams.models import Match, Tournament


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Użytkownik")
    points = models.PositiveIntegerField(verbose_name="Liczba punktów",default=0)
    joined = models.DateTimeField(verbose_name="Data dołączenia do ligi", auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        ordering = ("-points",)


class League(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=30)
    created = models.DateTimeField(verbose_name="Data dodania", auto_now_add=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name="Zawody")
    contestants = models.ManyToManyField(User, blank=True, verbose_name="Uczestnicy")

    def __str__(self):
        return f'{self.name} in {self.tournament}'

    class Meta:
        ordering = ("-created",)


class Bet(models.Model):
    date = models.DateTimeField(verbose_name="Data dodania", auto_now_add=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name="Mecz")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")
    playerOnePrediction = models.PositiveIntegerField(verbose_name="Wynik zawodnika 1", default=0)
    playerTwoPrediction = models.PositiveIntegerField(verbose_name="Wynik zawodnika 2", default=0)

    def __str__(self):
        return f'{self.user} on {self.match}'

    class Meta:
        ordering = ("-date",)


