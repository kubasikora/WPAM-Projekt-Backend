from django.contrib import admin
from betting import models


@admin.register(models.Bet)
class BetAdminView(admin.ModelAdmin):
    list_display = ("participant", "date")
    search_fields = ("participant", )


@admin.register(models.League)
class LeagueAdminView(admin.ModelAdmin):
    list_display = ("name", "created", "tournament", "leagueKey", "number_matches", "number_users")
    search_fields = ("name", "tournament")

    def number_matches(self, obj):
        return len(obj.tournament.matches.get_queryset())

    def number_users(self, obj):
        return len(obj.participants.get_queryset())


@admin.register(models.Participant)
class ParticipantAdminView(admin.ModelAdmin):
    list_display = ("user", "joined", "number_bets")
    search_fields = ("user",)

    def number_bets(self, obj):
        return len(obj.bets.get_queryset())