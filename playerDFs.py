# SINGLE CELL
import pandas as pd
import numpy as np
import re
import pickle

data = pd.read_csv("dataAll.csv")
data['seasonGW'] = data['season'].astype(str) + data["GW"].astype(str)

sgw = list(data.seasonGW.unique())

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

sgw.sort(key=natural_keys)
#print(sgw)

rank = zip(sgw, range(152))
dic = dict(rank)

playerDict = {}
Flag = pd.DataFrame(pd.Series(data.seasonGW.unique()), columns=['seasonGW'])
for p in  data.full_name.unique():
    playerDict[p] = data.loc[data.full_name == p].sort_values(by=['season', "GW"])
    playerDict[p] = playerDict[p].merge(Flag, how='right')
    playerDict[p]['seq'] = playerDict[p]['seasonGW'].map(dic)
    playerDict[p].sort_values(by=['seq'], inplace=True)
    playerDict[p].drop_duplicates(subset=['seq'], inplace=True)
    playerDict[p].reset_index(drop=True, inplace=True)
    
keep = ['full_name', 'season', 'GW', 'assists',
       'bonus', 'clean_sheets', 'element', 'goals_conceded', 'goals_scored',
       'minutes', 'own_goals', 'penalties_conceded', 'penalties_missed',
       'penalties_saved', 'red_cards', 'saves', 'total_points',
       'value', 'yellow_cards', 'position', 'seasonGW',
       'seq']

for p in playerDict.keys():
    playerDict[p] = playerDict[p][keep]
    
print(set([playerDict[p].shape for p in playerDict.keys()]))


with open('playerDict.pickle', 'wb') as handle:
    pickle.dump(playerDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

if False:
    with open('playerDict.pickle', 'rb') as handle:
        b = pickle.load(handle)
