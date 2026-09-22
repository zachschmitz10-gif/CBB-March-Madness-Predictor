# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:16:28 2026

@author: Zach Schmitz
"""

#%% Library Imports
import os
from pathlib import Path
from dotenv import load_dotenv 
import cbbd
from cbbd.rest import ApiException
import requests
import pandas as pd

#%% API Calls
load_dotenv()
YOUR_API_KEY = os.getenv('CBBD_API_KEY')


url = "https://api.collegebasketballdata.com/games"
params = {"season": 2027, "team": "Minnesota"}
headers = {"Authorization": f"Bearer {YOUR_API_KEY}"}

response = requests.get('https://api.collegebasketballdata.com/teams', headers=headers)
teams = response.json()

response = requests.get('https://api.collegebasketballdata.com/conferences', headers=headers)
confs = response.json()

d1_confs = []
for i in confs:
    d1_confs.append(i['shortName'])
    
d1_teams = []
for i in teams:
    if i['conference'] in d1_confs:
        print(i['school'])
        d1_teams.append(i['school'])
        


#%% ESPN API Direct?
espn_url = 'https://site.api.espn.com/apis/v2/sports/basketball/mens-college-basketball/standings'

req = requests.get(espn_url)
conf = req.json()
i = 0
team_abbrs = []
team_Ids_full = []
for ind in conf['children']:
    conference = ind['standings']
    for team in conference['entries']:
        abbr = team['team']['abbreviation']
        teamId = team['team']['id']
        team_abbrs.append(abbr)
        team_Ids_full.append(teamId)
        print(abbr, ", ", teamId)
        i += 1

print(i, "D1 CBB teams")

abbrs_Ids = []
for ind in range(len(team_abbrs)):
    abbrs_Ids.append((team_abbrs[ind], team_Ids_full[ind]))
