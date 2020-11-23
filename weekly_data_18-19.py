url_19 = "https://raw.githubusercontent.com/colinpbowen/fantasy-RL/main/data1819.csv"
df_19 = pd.read_csv(url_19)
df_19 = df_19.drop_duplicates(['player_id','round'])
player_minute_totals = df_19.pivot(index='player_id',columns='round',values='minutes')

