#import fixture data

import requests
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
url = 'https://fantasy.premierleague.com/api/fixtures'
r = requests.get(url)
json = r.json()
#print([i for i in json[0]])

fixture_df = pd.DataFrame({'matchweek': [], 'home_team': [], 'home_score':[], 'home_difclty':[], 
'away_team':[], 'away_score':[], 'away_difclty':[]}) #observations are fixtures, features are scores and stats.
for i in range(len(json)):
	if json[i]['finished'] == True:
		fixture_df.loc[i] = [json[i]['event'], 
			json[i]['team_h'], json[i]['team_h_score'], json[i]['team_h_difficulty'], 
			json[i]['team_a'], json[i]['team_a_score'], json[i]['team_a_difficulty']
			]
		#fixture_df = fixture_df.append(, ignore_index=True)
		#print(json[i]['event']) # this is the game week
		#print(json[i]['team_h'])
		#print(json[i]['team_a'])
		#for j in range(len(json[i]['stats'])):
		#	print(json[i]['stats'][j]['identifier'])


fixture_df.to_csv("FPLFixtureData.csv")

#print(fixture_df)