from django.contrib import admin
from betting import models


@admin.register(models.Bet)
class BetAdminView(admin.ModelAdmin):
    list_display = ("participant", "date")
    search_fields = ("participant", )


@admin.register(models.League)
class LeagueAdminView(admin.ModelAdmin):
    list_display = ("name", "created", "tournament")
    search_fields = ("name", "tournament")


@admin.register(models.Participant)
class ParticipantAdminView(admin.ModelAdmin):
    list_display = ("user", "joined")
    search_fields = ("user",)
