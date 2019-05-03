from django.db import models
'''
      "81845": {
        "fixture_id": "81845",
        "event_timestamp": "1556496000",
        "event_date": "2019-04-29T00:00:00+00:00",
        "league_id": "303",
        "round": "Primera Division - Round 10",
        "homeTeam_id": "2330",
        "awayTeam_id": "2318",
        "homeTeam": "Coquimbo Unido",
        "awayTeam": "Palestino",
        "status": "Match Finished",
        "statusShort": "FT",
        "goalsHomeTeam": "2",
        "goalsAwayTeam": "2",
        "halftime_score": "1-0",
        "final_score": "2 - 2",
        "penalty": "-",
        "elapsed": "90",
        "firstHalfStart": "1556496000",
        "secondHalfStart": "1556499600"
      },
'''
class Fixture(models.Model):
    fixture_id = models.IntegerField(default=0)
    event_timestamp = models.IntegerField(default=0)
    event_date = models.DateField(blank=True, null=True)
    league_id = models.IntegerField(blank=True, null=True)
    homeTeam_id = models.IntegerField(blank=True, null=True)
    awayTeam_id = models.IntegerField(blank=True, null=True)
    homeTeam = models.CharField(max_length=150, blank=True, null=True)
    awayTeam = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=150,blank=True, null=True)
    statusShort = models.CharField(max_length=15,blank=True, null=True)
    goalsHomeTeam = models.IntegerField(blank=True, null=True)
    goalsAwayTeam = models.IntegerField(blank=True, null=True)
    halftime_score = models.CharField(max_length=15,blank=True, null=True)
    final_score = models.CharField(max_length=15, blank=True, null=True)
    penalty = models.CharField(max_length=15, blank=True, null=True)
    elapsed = models.CharField(max_length=15, blank=True, null=True)
    firstHalfStart = models.CharField(max_length=15, blank=True, null=True)
    secondHalfStart = models.CharField(max_length=15, blank=True, null=True)   