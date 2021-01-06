from django.contrib import admin
from teams import models

@admin.register(models.Country)
class CountryAdminView(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")

@admin.register(models.Tournament)
class TournamentAdminView(admin.ModelAdmin):
    list_display = ("name", "sport", "domestic", "finished")
    search_fields = ("name",)
    list_filter = ("finished", "sport")

@admin.register(models.Contestant)
class ContestantAdminView(admin.ModelAdmin):
    list_display = ("name", "country", "sport")
    search_fields = ("name",)
    list_filter = ("country", "sport")

@admin.register(models.Venue)
class VenueAdminView(admin.ModelAdmin):
    list_display = ("name", "city", "country")
    search_fields = ("name",)

@admin.register(models.Match)
class MatchAdminView(admin.ModelAdmin):
    list_display = ("wynik", "playerOne", "playerTwo", "finished", "tournament", "venue", "dateOfStart")
    search_fields = ("playerOne", "playerTwo")
    list_filter = ("finished",)

    def wynik(self, obj):
        return f"{obj.playerOneResult} : {obj.playerTwoResult}"