from django.contrib import admin
from betting import models

@admin.register(models.Bet)
class BetAdminView(admin.ModelAdmin):
    list_display = ("user", "date")
    search_fields = ("user", )

# Register your models here.
