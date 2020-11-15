from django.db import models

class Country(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=20)
    code = models.CharField(verbose_name="Skrót", max_length=4, )

    def __str__(self):
        return f"{self.code}"

    class Meta:
        ordering = ("name", "code")
        verbose_name_plural = "Countries"


class Sport(models.Model):
    name = models.CharField(verbose_name="Dyscyplina", max_length=20)
    created = models.DateTimeField(verbose_name="Czas dodania", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created", "name")


class League(models.Model):
    entryCode = models.CharField(verbose_name="Kod", max_length=7)
    name = models.CharField(verbose_name="Nazwa", max_length=30)
    created = models.DateTimeField(verbose_name="Czas dodania", auto_now_add=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="leagues", verbose_name="Dyscyplina")
    domestic = models.BooleanField(default=True, verbose_name="Liga krajowa")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created", "name")


class Team(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=100)
    created = models.DateTimeField(verbose_name="Czas dodania", auto_now_add=True)
    league = models.ManyToManyField(League, verbose_name="Liga")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="teams")
    
    def __str__(self):
        return f"{self.name} ({self.country})"

    class Meta:
        ordering = ("-created", "name")
