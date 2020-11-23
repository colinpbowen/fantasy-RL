#read in the FPL API
import requests
import pandas as pd
import numpy as np

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json = r.json()
#print(json.keys())

elements = pd.DataFrame(json['elements'])
element_types = pd.DataFrame(json['element_types'])
teams = pd.DataFrame(json['teams'])


#elite selected players
elite_select = pd.read_csv("elite_selection_GW9.csv")
#print(teams['name'])
second_name = elements['second_name']
selected_by_percent = elements['selected_by_percent']
#print(elements.columns)
elements1 = elements[['web_name','team','element_type', 'selected_by_percent', 'now_cost','minutes', 
'transfers_in', 'value_season', 'total_points', 'ict_index_rank', 'chance_of_playing_next_round']]


elements1['position']= elements1.element_type.map(element_types.set_index('id').singular_name)
elements1['club'] = elements1.team.map(teams.set_index('id').name)
elements1 = elements1.merge(elite_select, how='left', on='web_name')

#exclude James McCarthy from the merge error
mccarthy_cp = (elements1.web_name == "McCarthy") & (elements1.team == 6)
elements1['elite_selected'][mccarthy_cp] = 0
#elements1[elements1.second_name == "Salah"]

#this excludes united, villa, burnley, and city
#bool_vec = (elements1.team == 13) | (elements1.team == 12) | (elements1.team == 2) | (elements1.team == 4)
#elements1.now_cost[bool_vec] = 1000
#elements1['now_cost'].iloc[elements1['team']== 13 | elements1['team'] == 12 | 
#	elements1['team'] == 2 | elements1['team'] == 4] = 1000
elements1.to_csv("FPLPlayerData2.csv", sep = ",")
#print(elements1.head())