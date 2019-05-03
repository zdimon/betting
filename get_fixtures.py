import os
import datetime
from time import strftime
from datetime import timedelta
import requests
from settings import API_HOST, API_KEY

DATA_DIR = 'data'
if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)

date_range = []
now = datetime.datetime.now()
for n in range(1,4):
    dt = now - timedelta(days=n)
    date_range.append(dt.strftime("%Y-%m-%d"))


headers={
    "X-RapidAPI-Host": API_HOST,
    "X-RapidAPI-Key": API_KEY
  }


#print(date_range)
for date in date_range:
    url = 'https://api-football-v1.p.rapidapi.com/fixtures/date/%s' % date
    r = requests.get(url,headers=headers)
    filename = '%s/%s.json' % (DATA_DIR,date)
    with open(filename,'w+') as f:  
        f.write(r.text)
    print("Saving....%s" % filename)