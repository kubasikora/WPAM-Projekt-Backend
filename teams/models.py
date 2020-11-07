from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=100)
    created = models.DateTimeField(verbose_name="Czas dodania", auto_now_add=True)

    class Meta:
        ordering = ("-created", "name")