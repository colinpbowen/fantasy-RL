player_ids_1819 = pd.read_csv("https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2018-19/player_idlist.csv")
full_names = []
for i in range(len(player_ids_1819)):
    ls = list(player_ids_1819.iloc[i,:].values)
    string = player_ids_1819.iloc[i,0]+ "_" + player_ids_1819.iloc[i,1] + "_" + player_ids_1819.iloc[i,2].astype(str)
    full_names.append(string)
    
base_str = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2018-19/players/"
#Aaron_Cresswell_402/gw.csv"
selected = []
cost = []
for player in full_names:
    #try:
    url = base_str + player +"/gw.csv"
    print(url)
    df = pd.read_csv(url,encoding='ISO-8859-1')
    #except:
    #    print(base_str + player +"/gw.csv")
        
    try:
        idx = df['round'] == 1
        selected.append(df.selected[idx][0])
        cost.append(df.value[idx][0])
    except IndexError:
        print(player)
        selected.append(0)
        cost.append(0)
