from django.db import models
from django.utils.translation import gettext_lazy as _

class Country(models.Model):
    name = models.CharField(verbose_name="Name", max_length=20)
    code = models.CharField(verbose_name="Code", max_length=4)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("name", "code")
        verbose_name_plural = "Countries"


class Sport(models.TextChoices):
    FOOTBALL = "FOOTBALL", _("Piłka nożna")
    VOLLEYBALL = "VOLLEYBALL", _("Siatkówka")
    TENNIS = "TENNIS", _("Tenis")


class Venue(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    city = models.CharField(verbose_name="City", max_length=25)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country")
    longitude = models.FloatField(verbose_name="Longitude", max_length=10)
    latitude = models.FloatField(verbose_name="Latitude", max_length=10)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} ({self.city})"

class Contestant(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country", related_name="teams")
    sport = models.CharField(verbose_name="Sport", choices=Sport.choices, default=Sport.FOOTBALL, max_length=15)

    def __str__(self):
        return f"{self.name} ({self.country.code})"

    class Meta:
        ordering = ("-created", "name")


class Tournament(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    dateOfStart = models.DateTimeField(verbose_name="Time of start")
    sport = models.CharField(verbose_name="Sport", choices=Sport.choices, default=Sport.FOOTBALL, max_length=15)
    contestants = models.ManyToManyField(Contestant, blank=True, verbose_name="Contestants")
    domestic = models.BooleanField(default=True, verbose_name="Is domestic league")
    finished = models.BooleanField(default=False, verbose_name="Is finished")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created", "name")


class Result(models.TextChoices):
    NOT_PLAYED = "N", _("N")
    ONE = "1", _("1")
    TWO = "2", _("2")
    DRAW = "X", _("X")


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name="Tournament", related_name="matches")
    playerOne = models.ForeignKey(Contestant, on_delete=models.CASCADE, verbose_name="Contestant 1", related_name="playerOnes")
    playerTwo = models.ForeignKey(Contestant, on_delete=models.CASCADE, verbose_name="Contestant 2", related_name="playerTwos")
    dateOfStart = models.DateTimeField(verbose_name="Time of start")
    sport = models.CharField(verbose_name="Sport", choices=Sport.choices, default=Sport.FOOTBALL, max_length=15)
    playerOneResult = models.PositiveIntegerField(verbose_name="Score 1", default=0)
    playerTwoResult = models.PositiveIntegerField(verbose_name="Score 2", default=0)
    outcome = models.CharField(verbose_name="Result", choices=Result.choices, default=Result.NOT_PLAYED, max_length=1)
    finished = models.BooleanField(default=False, verbose_name="Is finished")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, verbose_name="Venue", null=True, blank=True)

    class Meta:
        ordering = ("-dateOfStart",)
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"{self.playerOne} vs {self.playerTwo}"
