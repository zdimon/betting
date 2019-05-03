from django.core.management.base import BaseCommand, CommandError
import json
from bet.models import Fixture
from datetime import timedelta
import requests
from dj_prj.settings import API_HOST, API_KEY

headers={
    "X-RapidAPI-Host": API_HOST,
    "X-RapidAPI-Key": API_KEY
  }


class Command(BaseCommand):

    def handle(self, *args, **options):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        print('Loading fixtures %s' % now)   
        url = 'https://api-football-v1.p.rapidapi.com/fixtures/date/%s' % now
        r = requests.get(url,headers=headers)
        jsdata = json.loads(r.text)
        #with open('../data/2019-04-29.json','r') as f:
        #    txt = f.read()
        #    jsdata = json.loads(txt)
        for d in jsdata['api']['fixtures']:
            it = jsdata['api']['fixtures'][d]
            f = Fixture()
            f.fixture_id = it['fixture_id']
            f.event_timestamp = it['event_timestamp']
            f.event_date = it['event_date'][0:9]
            f.league_id = it['league_id']
            f.homeTeam_id = it['homeTeam_id']
            f.awayTeam_id = it['awayTeam_id']
            f.homeTeam = it['homeTeam']
            f.awayTeam = it['awayTeam']
            f.status = it['status']
            f.statusShort = it['statusShort']
            f.goalsHomeTeam = it['goalsHomeTeam']
            f.goalsAwayTeam = it['goalsAwayTeam']
            f.halftime_score = it['halftime_score']
            f.final_score = it['final_score']
            f.penalty = it['penalty']
            f.elapsed = it['elapsed']
            f.firstHalfStart = it['firstHalfStart'] 
            f.secondHalfStart = it['secondHalfStart'] 
            f.save()
            print("Saving....%s" % f.fixture_id)