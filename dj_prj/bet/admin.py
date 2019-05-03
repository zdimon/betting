from django.contrib import admin

from bet.models import Fixture

class FixtureAdmin(admin.ModelAdmin):
    list_display = ['homeTeam', 'awayTeam', 'goalsHomeTeam', 'goalsAwayTeam']

admin.site.register(Fixture, FixtureAdmin)