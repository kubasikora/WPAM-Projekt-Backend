from django.contrib import admin
from teams import models

@admin.register(models.Team)
class TeamAdminView(admin.ModelAdmin):
    list_display = ("name", "created")
    search_fields = ("name",)
