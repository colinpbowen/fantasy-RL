import pandas as pd
import numpy as np

data = pd.read_csv("dataAll.csv")
print(data.columns)
data.head()

data['seasonGW'] = data['season'].astype(str) + data["GW"].astype(str)
data

playerDict = {}
for p in  data.full_name.unique():
    playerDict[p] = data.loc[data.full_name == "Aaron_Cresswell"].sort_values(by=['season', "GW"])

import pickle

with open('playerDict.pickle', 'wb') as handle:
    pickle.dump(playerDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('playerDict.pickle', 'rb') as handle:
    b = pickle.load(handle)
    
