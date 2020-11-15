from django.contrib import admin
from teams import models

@admin.register(models.Country)
class CountryAdminView(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")

@admin.register(models.Sport)
class SportAdminView(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(models.League)
class LeagueAdminView(admin.ModelAdmin):
    list_display = ("name", "sport", "domestic", "entryCode", "created")
    search_fields = ("name", "entryCode")

@admin.register(models.Team)
class TeamAdminView(admin.ModelAdmin):
    list_display = ("name", "created")
    search_fields = ("name",)