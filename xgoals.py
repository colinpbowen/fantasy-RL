import pandas as pd
import numpy as np





def xGprobs(df, week):
    """
    Calculate distribution of expected goals for a player. 
    Args: df (player's gw DataFrame) ,week (int)
    """
    gs = df['goals_scored'][0:week+1].value_counts().sort_index()
    if gs.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0, 0, 0]  # Some prior we can change later. This assume p(0 Goals) = 1
    else:
        idx = pd.DataFrame(index=np.arange(4+1))
        stats = idx.join(gs).fillna(0)
        return [stats.goals_scored[x]/stats.goals_scored.sum() for x in range(len(stats))]

# ## Expected Assists
def xAprobs(df, week):
    """
    Calculate distribution of expected assists for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    ass = df['assists'][0:week+1].value_counts().sort_index()
    if ass.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0, 0]  # Some prior we can change later. This assume p(0 assists) = 1
    else:
        idx = pd.DataFrame(index=np.arange(3+1))
        stats = idx.join(ass).fillna(0)
        return [stats.assists[x]/stats.assists.sum() for x in range(len(stats))]

# ## Expected Bonus
def xBprobs(df, week):
    """
    Calculate distribution of expected bonus for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    bon = df['bonus'][0:week+1].value_counts().sort_index()
    if bon.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0, 0]  # Some prior we can change later. This assume p(0 bonus) = 1
    else:
        idx = pd.DataFrame(index=np.arange(3+1))
        stats = idx.join(bon).fillna(0)
        return [stats.bonus[x]/stats.bonus.sum() for x in range(len(stats))]

# ## Expected Clean Sheets

def xCSprobs(df, week):
    """
    Calculate distribution of expected clean sheets for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    cs = df['clean_sheets'][0:week+1].value_counts().sort_index()
    if cs.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(cs).fillna(0)
        return [stats.clean_sheets[x]/stats.clean_sheets.sum() for x in range(len(stats))]


# ## Expected Goals Conceded
def xGCprobs(df, week):
    """
    Calculate distribution of expected goals conceded for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    gc = df['goals_conceded'][0:week+1].value_counts().sort_index()
    if gc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0., 0., 0., 0., 0., 0., 0., 0., 0.]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(9+1))
        stats = idx.join(gc).fillna(0)
        return [stats.goals_conceded[x]/stats.goals_conceded.sum() for x in range(len(stats))]


# ## Expected Minutes


def xMprobs(df, week):
    """
    Calculate distribution of expected minutes for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    p = np.zeros(91)
    p[0] = 1.0
    M = df['minutes'][0:week+1].value_counts().sort_index()
    if M.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return p  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(90+1))
        stats = idx.join(M).fillna(0)
        return [stats.minutes[x]/stats.minutes.sum() for x in range(len(stats))]


# ## Expected Own Goals


def xOGprobs(df, week):
    """
    Calculate distribution of expected own goals for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    og = df['own_goals'][0:week+1].value_counts().sort_index()
    if og.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(og).fillna(0)
        return [stats.own_goals[x]/stats.own_goals.sum() for x in range(len(stats))]



# ## Expected Penalties Conceded


def xPCprobs(df, week):
    """
    Calculate distribution of expected penalties conceded for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    pc = df['penalties_conceded'][0:week+1].value_counts().sort_index()
    if pc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(2+1))
        stats = idx.join(pc).fillna(0)
        return [stats.penalties_conceded[x]/stats.penalties_conceded.sum() for x in range(len(stats))]


# ## Expected Penalties Missed

def xPMprobs(df, week):
    """
    Calculate distribution of expected penalties missed for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    pm = df['penalties_missed'][0:week+1].value_counts().sort_index()
    if pm.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(pm).fillna(0)
        return [stats.penalties_missed[x]/stats.penalties_missed.sum() for x in range(len(stats))]

# ## Expected Penalties Saved

def xPSprobs(df, week):
    """
    Calculate distribution of expected penalties saved for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    ps = df['penalties_saved'][0:week+1].value_counts().sort_index()
    if ps.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(2+1))
        stats = idx.join(ps).fillna(0)
        return [stats.penalties_saved[x]/stats.penalties_saved.sum() for x in range(len(stats))]




# ## Expected Red Cards

def xRCprobs(df, week):
    """
    Calculate distribution of expected red cards for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    rc = df['red_cards'][0:week+1].value_counts().sort_index()
    if rc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(rc).fillna(0)
        return [stats.red_cards[x]/stats.red_cards.sum() for x in range(len(stats))]



# ## Expected Saves

def xSprobs(player, week):
    """
    Calculate distribution of expected saves for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    p = np.zeros(15)
    p[0] = 1.0
    s = df['saves'][0:week+1].value_counts().sort_index()
    if s.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return p  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(14+1))
        stats = idx.join(s).fillna(0)
        return [stats.saves[x]/stats.saves.sum() for x in range(len(stats))]


# ## Expected Yellow Cards


def xYCprobs(player, week):
    """
    Calculate distribution of expected yellow cards for a player. 
    Args: df (player's gw DataFrame), week (int)
    """
    yc = df['yellow_cards'][0:week+1].value_counts().sort_index()
    if yc.empty == True:  ## WHEN WE DON'T HAVE ANY DATA
        return [1, 0]  # Some prior we can change later. This assume p(0 CS) = 1
    else:
        idx = pd.DataFrame(index=np.arange(1+1))
        stats = idx.join(yc).fillna(0)
        return [stats.yellow_cards[x]/stats.yellow_cards.sum() for x in range(len(stats))]
        
        
        
        
#expected points
def getXpts(df, week, position):
    """
    Generate simulation outcome for a particular week based upon prior distributions.
    """
    import np.random.choice as ch
    with (df, week) as a:
        xG = XGprobs(a)
        xA = XAprobs(a)
        xB = xBprobs(a)
        xCS = xCSprobs(a)
        xGC = xGCprobs(a)
        xM = xMprobs(a)
        xOG = xOGprobs(a)
        xPC = xPCprobs(a)
        xPM = xPMprobs(a)
        xPS = xPSprobs(a)
        xRC = xRCprobs(a)
        xS = xSprobs(a)
        xYC = xYCprobs(a)
    
    G = ch(p=xG)
    A = ch(p=xA)
    B = ch(p=xB)
    CS = ch(p=xCS)
    GC = ch(p=xGC)
    M = ch(p=xM)
    OG = ch(p=xOG)
    PC = ch(p=xPC)
    PM = ch(p=xPM)
    PS = ch(p=xPS)
    RC = ch(p=xRC)
    S = ch(p=xS)
    YC = ch(xYC)
    data = {'goals_scored':G, 'assists': A,'bonus': B,'clean_sheets': CS,'goals_conceded': GC,
            'minutes': M,'own_goals': OG,'penalties_conceded': PC,'penalties_missed': PM,
            'penalties_saved': PS, 'red_cards': RC, 'saves' : S,'yellow_cards' : YC}
    return getPts(data, position)

#generate realization
#no need to use this for accessing historical data because it's already stored? 
#need to add penalties conceded
def getPts(x, position):
    """ 
    Use with getXpts for simulating reward.
    """
    pts = 0
    pts += x['bonus']
    if (x['minutes'] > 0 & x['minutes'] < 60):
        pts += 1
    elif x['minutes'] >=60:
        pts += 2
    if position == 1.0:  # Goalie
        pts += 6*x['goals_scored'] + x['assists']*3 + 4*x['clean_sheets'] + int(x['saves']//3) + 5*x['penalties_saved'] - x['goals_conceded']//2 - x['yellow_cards'] - 3*x['red_cards'] - 2*x['own_goals']   
    elif position == 2.0:  # Defender
        pts += 6*x['goals_scored'] + x['assists']*3 + 4*x['clean_sheets'] - 2*x['penalties_missed']  - x['goals_conceded']//2 - x['yellow_cards'] - 3*x['red_cards'] - 2*x['own_goals']
    elif position == 3.0: # Mid
        pts += 5*x['goals_scored'] + x['assists']*3 + 1*x['clean_sheets'] - 2*x['penalties_missed'] - x['yellow_cards'] - 3*x['red_cards'] - 2*x['own_goals']
    else:  # Striker
        pts += 4*x['goals_scored'] + x['assists']*3 - 2*x['penalties_missed'] - x['yellow_cards'] - 3*x['red_cards'] - 2*x['own_goals']
    return pts
    
