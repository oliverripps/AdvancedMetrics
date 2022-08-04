import pandas as pd
import playermetrics

file = open("Returners_Stats.csv")
df = pd.read_csv(file)
player_dataframe = df
TS_sum= 0
players = len(df)
for player_stats in df.iterrows():
    stats = player_stats[1]
    print(stats)
    name = stats[1]
    PTS = stats[24]
    FGA = stats[7]
    FTA = stats[13]
    TS = playermetrics.TS(PTS,FGA,FTA)
    TS_sum += TS
    #print(name,":", TS)
average_ts = TS_sum/players

for player_stats in df.iterrows():
    stats = player_stats[1]
    name = stats[1]
    PTS = stats[24]
    FGA = stats[7]
    FTA = stats[13]
    TS = round(playermetrics.TS(PTS,FGA,FTA), 4)
    #TS PLUS WILL HAVE TO INCLUDE ALL PLAYERS NOT JUST RETURNERS
    #MUST KEEP RETURNERS IN DATASET AND HAVE AN ATTRIBUTE NOT TO SHOW THEIR RESULTS BUT INCLUDE IN AVERAGE
    TS_PLUS = round(TS/average_ts * 100)
    #print(name,":", TS_PLUS)

#print(average_ts)