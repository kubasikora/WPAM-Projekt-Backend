from django.contrib import admin
from teams import models

@admin.register(models.Country)
class CountryAdminView(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")

@admin.register(models.Tournament)
class TournamentAdminView(admin.ModelAdmin):
    list_display = ("name", "sport", "domestic", "created")
    search_fields = ("name",)

@admin.register(models.Contestant)
class ContestantAdminView(admin.ModelAdmin):
    list_display = ("name", "created")
    search_fields = ("name",)

@admin.register(models.Match)
class MatchAdminView(admin.ModelAdmin):
    list_display = ("dateOfStart", "playerOne", "playerTwo", "matchResult")
    search_fields = ("playerOne", "playerTwo")

    def matchResult(self, obj):
        return f"{obj.playerOneResult} : {obj.playerTwoResult}"