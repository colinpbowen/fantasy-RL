# SINGLE CELL
import pandas as pd
import numpy as np
import re
import pickle

data = pd.read_csv("dataAll.csv")
data['seasonGW'] = data['season'].astype(str) + data["GW"].astype(str)

#sgw = list(data.seasonGW.unique())

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]
sgw = ['16171',
 '16172',
 '16173',
 '16174',
 '16175',
 '16176',
 '16177',
 '16178',
 '16179',
 '161710',
 '161711',
 '161712',
 '161713',
 '161714',
 '161715',
 '161716',
 '161717',
 '161718',
 '161719',
 '161720',
 '161721',
 '161722',
 '161723',
 '161724',
 '161725',
 '161726',
 '161727',
 '161728',
 '161729',
 '161730',
 '161731',
 '161732',
 '161733',
 '161734',
 '161735',
 '161736',
 '161737',
 '161738',
 '17181',
 '17182',
 '17183',
 '17184',
 '17185',
 '17186',
 '17187',
 '17188',
 '17189',
 '171810',
 '171811',
 '171812',
 '171813',
 '171814',
 '171815',
 '171816',
 '171817',
 '171818',
 '171819',
 '171820',
 '171821',
 '171822',
 '171823',
 '171824',
 '171825',
 '171826',
 '171827',
 '171828',
 '171829',
 '171830',
 '171831',
 '171832',
 '171833',
 '171834',
 '171835',
 '171836',
 '171837',
 '171838',
 '18191',
 '18192',
 '18193',
 '18194',
 '18195',
 '18196',
 '18197',
 '18198',
 '18199',
 '181910',
 '181911',
 '181912',
 '181913',
 '181914',
 '181915',
 '181916',
 '181917',
 '181918',
 '181919',
 '181920',
 '181921',
 '181922',
 '181923',
 '181924',
 '181925',
 '181926',
 '181927',
 '181928',
 '181929',
 '181930',
 '181931',
 '181932',
 '181933',
 '181934',
 '181935',
 '181936',
 '181937',
 '181938',
 '19201',
 '19202',
 '19203',
 '19204',
 '19205',
 '19206',
 '19207',
 '19208',
 '19209',
 '192010',
 '192011',
 '192012',
 '192013',
 '192014',
 '192015',
 '192016',
 '192017',
 '192018',
 '192019',
 '192020',
 '192021',
 '192022',
 '192023',
 '192024',
 '192025',
 '192026',
 '192027',
 '192028',
 '192029',
 '192030',
 '192031',
 '192032',
 '192033',
 '192034',
 '192035',
 '192036',
 '192037',
 '192038']

#sgw.sort(key=natural_keys)
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
       'penalties_saved', 'red_cards', 'saves', 'selected', 'total_points',
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
