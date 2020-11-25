#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pickle
import re
import matplotlib.pyplot as plt


# In[ ]:


if False:
    data = pd.read_csv("dataAll.csv")
    data.columns
    squads = pd.read_csv('player_squad_mapping.csv')
    sdic1= dict(zip(list(squads.full_name[0:499]), list(squads.squad[0:499])))
    sdic2= dict(zip(list(squads.full_name[499:]), list(squads.squad[499:])))

    data["squad"] = [data.full_name.map(sdic1) if data.season[x] < 1920 else data.full_name.map(sdic2) for x in range(len(data))]


# In[71]:


data = pd.read_csv('dataAll.csv')
data.max()


# In[93]:


data2 = data.loc[data.minutes >= 60]
data2


# In[103]:


data2.quantile(q=0.999)


# # Visualize historical distributions

# ## Goals conceded (0-7)

# In[97]:


plt.style.use('seaborn')
plt.hist(data2.goals_conceded)


# ## Assists (0-2)

# In[98]:


plt.hist(data2.assists)


# ## Minutes

# In[99]:


plt.hist(data2.minutes)


# ## Saves

# In[105]:


plt.hist(data2.saves)


# In[13]:


with open('playerDict.pickle', 'rb') as handle:
    playerDict = pickle.load(handle)


# In[29]:


for p in playerDict.keys:
    playerDic


# In[188]:


ms = playerDict["Mohamed_Salah"]
ms.loc[ms.isnull().any(axis=1)]


# In[81]:


#pd.pivot_table(ms, values=['assists'], index=['seq'], aggfunc=[np.cumsum,]).reset_index()


# In[178]:


ms['assists'][0:2].value_counts()
print(ms['goals_scored'][0:2].value_counts().empty)
d = ms['goals_scored'][0:80].value_counts().sort_index()
print(d.empty)

#b = pd.Series(index=(np.array(range((d.index.max()+1)))))
#print(d.index.max())
#d
print(d)
b = pd.DataFrame(index=np.arange(4+1))
print(b)
bd = b.join(d).fillna(0)
print(bd)
[bd.goals_scored[x]/bd.goals_scored.sum() for x in range(len(bd))]


# ## Expected Goals Scored

# In[195]:


def xGS(player, week):
    """
    Calculate distribution of expected goals for a player. Input a full_name and week (seq)
    """
    gs = playerDict[player]['goals_scored'][0:week+1].value_counts().sort_index()
    if gs.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0, 0, 0]  # Some prior we can change later. This assume p(0 Goals) = 1
    else:
        idx = pd.DataFrame(index=np.arange(4+1))
        stats = idx.join(gs).fillna(0)
        return [stats.goals_scored[x]/stats.goals_scored.sum() for x in range(len(stats))]


# In[196]:


print(xGS('Mohamed_Salah',79))
print(xGS('Mohamed_Salah',132))


# ## Expected Assists

# In[197]:


def xA(player, week):
    """
    Calculate distribution of expected assists for a player. Input a full_name and week (seq)
    """
    ass = playerDict[player]['assists'][0:week+1].value_counts().sort_index()
    if ass.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0, 0]  # Some prior we can change later. This assume p(0 assists) = 1
    else:
        idx = pd.DataFrame(index=np.arange(3+1))
        stats = idx.join(ass).fillna(0)
        return [stats.assists[x]/stats.assists.sum() for x in range(len(stats))]


# In[198]:


print(xA('Mohamed_Salah',79))
print(xA('Mohamed_Salah',132))


# ## Expected Bonus

# In[199]:


def xB(player, week):
    """
    Calculate distribution of expected bonus for a player. Input a full_name and week (seq)
    """
    bon = playerDict[player]['bonus'][0:week+1].value_counts().sort_index()
    if bon.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0, 0]  # Some prior we can change later. This assume p(0 bonus) = 1
    else:
        idx = pd.DataFrame(index=np.arange(3+1))
        stats = idx.join(bon).fillna(0)
        return [stats.bonus[x]/stats.bonus.sum() for x in range(len(stats))]


# In[200]:


print(xB('Mohamed_Salah',79))
print(xB('Mohamed_Salah',132))


# ## Expected Clean Sheets

# In[205]:


np.zeros(10)


# In[206]:


def xCS(player, week):
    """
    Calculate distribution of expected clean sheets for a player. Input a full_name and week (seq)
    """
    cs = playerDict[player]['clean_sheets'][0:week+1].value_counts().sort_index()
    if cs.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(cs).fillna(0)
        return [stats.clean_sheets[x]/stats.clean_sheets.sum() for x in range(len(stats))]


# In[207]:


print(xCS('Mohamed_Salah',79))
print(xCS('Mohamed_Salah',132))


# ## Expected Goals Conceded

# In[208]:


def xGC(player, week):
    """
    Calculate distribution of expected goals conceded for a player. Input a full_name and week (seq)
    """
    gc = playerDict[player]['goals_conceded'][0:week+1].value_counts().sort_index()
    if gc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0., 0., 0., 0., 0., 0., 0., 0., 0.]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(9+1))
        stats = idx.join(gc).fillna(0)
        return [stats.goals_conceded[x]/stats.goals_conceded.sum() for x in range(len(stats))]


# In[209]:


print(xGC('Mohamed_Salah',79))
print(xGC('Mohamed_Salah',132))


# ## Expected Minutes

# In[235]:


def xM(player, week):
    """
    Calculate distribution of expected minutes for a player. Input a full_name and week (seq)
    """
    p = np.zeros(91)
    p[0] = 1.0
    M = playerDict[player]['minutes'][0:week+1].value_counts().sort_index()
    if M.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return p  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(90+1))
        stats = idx.join(M).fillna(0)
        return [stats.minutes[x]/stats.minutes.sum() for x in range(len(stats))]


# In[236]:


print(xM('Mohamed_Salah',79))
sum(xM('Mohamed_Salah',132)[-30:])


# ## Expected Own Goals

# In[218]:


def xOG(player, week):
    """
    Calculate distribution of expected own goals for a player. Input a full_name and week (seq)
    """
    og = playerDict[player]['own_goals'][0:week+1].value_counts().sort_index()
    if og.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(og).fillna(0)
        return [stats.own_goals[x]/stats.own_goals.sum() for x in range(len(stats))]


# In[219]:


print(xOG('Mohamed_Salah',79))
xOG('Mohamed_Salah',4)


# ## Expected Penalties Conceded

# In[222]:


def xPC(player, week):
    """
    Calculate distribution of expected penalties conceded for a player. Input a full_name and week (seq)
    """
    pc = playerDict[player]['penalties_conceded'][0:week+1].value_counts().sort_index()
    if pc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(2+1))
        stats = idx.join(pc).fillna(0)
        return [stats.penalties_conceded[x]/stats.penalties_conceded.sum() for x in range(len(stats))]


# In[225]:


print(xPC('Mohamed_Salah',79))
xPC('Mohamed_Salah',4)


# ## Expected Penalties Missed

# In[226]:


def xPM(player, week):
    """
    Calculate distribution of expected penalties missed for a player. Input a full_name and week (seq)
    """
    pm = playerDict[player]['penalties_missed'][0:week+1].value_counts().sort_index()
    if pm.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(pm).fillna(0)
        return [stats.penalties_missed[x]/stats.penalties_missed.sum() for x in range(len(stats))]


# In[227]:


print(xPM('Mohamed_Salah',79))
xPM('Mohamed_Salah',4)


# ## Expected Penalties Saved

# In[228]:


def xPS(player, week):
    """
    Calculate distribution of expected penalties saved for a player. Input a full_name and week (seq)
    """
    ps = playerDict[player]['penalties_saved'][0:week+1].value_counts().sort_index()
    if ps.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(2+1))
        stats = idx.join(ps).fillna(0)
        return [stats.penalties_saved[x]/stats.penalties_saved.sum() for x in range(len(stats))]


# In[229]:


print(xPS('Mohamed_Salah',79))
xPS('Mohamed_Salah',4)


# ## Expected Red Cards

# In[232]:


def xRC(player, week):
    """
    Calculate distribution of expected red cards for a player. Input a full_name and week (seq)
    """
    rc = playerDict[player]['red_cards'][0:week+1].value_counts().sort_index()
    if rc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(rc).fillna(0)
        return [stats.red_cards[x]/stats.red_cards.sum() for x in range(len(stats))]


# In[234]:


print(xRC('Mohamed_Salah',151))
xRC('Mohamed_Salah',4)


# ## Expected Saves

# In[238]:


def xS(player, week):
    """
    Calculate distribution of expected saves for a player. Input a full_name and week (seq)
    """
    p = np.zeros(15)
    p[0] = 1.0
    s = playerDict[player]['saves'][0:week+1].value_counts().sort_index()
    if s.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return p  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(14+1))
        stats = idx.join(s).fillna(0)
        return [stats.saves[x]/stats.saves.sum() for x in range(len(stats))]


# In[239]:


print(xS('Mohamed_Salah',151))
xS('Mohamed_Salah',4)


# ## Expected Yellow Cards

# In[240]:


def xYC(player, week):
    """
    Calculate distribution of expected yellow cards for a player. Input a full_name and week (seq)
    """
    yc = playerDict[player]['yellow_cards'][0:week+1].value_counts().sort_index()
    if yc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(yc).fillna(0)
        return [stats.yellow_cards[x]/stats.yellow_cards.sum() for x in range(len(stats))]


# In[243]:


print(xYC('Mohamed_Salah',151))
xYC('Mohamed_Salah',4)


# ## Use the reference below to check maximum values for the above functions

# In[ ]:


first_name                   Ørjan
last_name                     Özil
assists                          3
bonus                            3
clean_sheets                     1
element                        680
goals_conceded                   9
goals_scored                     4
minutes                         90
own_goals                        1
penalties_conceded               2
penalties_missed                 1
penalties_saved                  2
red_cards                        1
GW                              38
saves                           14
selected                   3983614
total_points                    29
value                          136
yellow_cards                     1
season                        1920
player_id                      658


# ## Expected Points

# In[244]:


def getXpts(full_name):
    x = playerDict[full_name]
    pts = 0
    pts += x.bonus
    if (x.minutes > 0 & x.minutes < 60):
        pts += 1
    elif x.minutes >=60:
        pts += 2
    if x.position == 1.0:  # Goalie
        pts += 6*x.goals_scored + x.assists*3 + 4*x.clean_sheets + int(x.saves/3) + 5*x.penalties_saved - 2*int(x.goals_conceded/2) - x.yellow_cards - 3*x.red_cards - 2*x.own_goals   
    elif x.position == 2.0:  # Defender
        pts += 6*x.goals_scored + x.assists*3 + 4*x.clean_sheets - 2*x.penalties_missed  - 2*int(x.goals_conceded/2) - x.yellow_cards - 3*x.red_cards - 2*x.own_goals
    elif x.position == 3.0: # Mid
        pts += 5*x.goals_scored + x.assists*3 + 1*x.clean_sheets - 2*x.penalties_missed - x.yellow_cards - 3*x.red_cards - 2*x.own_goals
    else:  # Striker
        pts += 4*x.goals_scored + x.assists*3 - 2*x.penalties_missed - x.yellow_cards - 3*x.red_cards - 2*x.own_goals
    return pts
#data['points'] = data.apply(lambda x: getPoints(x), axis=1)

