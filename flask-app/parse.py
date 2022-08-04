import pandas as pd
import playermetrics

def parse(filename):
    #file = open("Returners_Stats.csv")
    file = open(filename)
    df = pd.read_csv(file)
    TS_sum= 0
    players = len(df)
    # initialize list of lists
    data = []
    
    #establish averages
    for player_stats in df.iterrows():
        stats = player_stats[1]
        name = stats[1]
        PTS = stats[25]
        FGA = stats[7]
        FTA = stats[13]
        TS = playermetrics.TS(PTS,FGA,FTA)
        TS_sum += TS
    average_ts = TS_sum/players

    #create data
    for player_stats in df.iterrows():
        player = []
        stats = player_stats[1]
        name = stats[1]
        PTS = stats[25]
        FGA = stats[7]
        FTA = stats[13]
        TS = round(playermetrics.TS(PTS,FGA,FTA), 4)
        print(name,PTS,FGA,FTA)
        #TS PLUS WILL HAVE TO INCLUDE ALL PLAYERS NOT JUST RETURNERS
        #MUST KEEP RETURNERS IN DATASET AND HAVE AN ATTRIBUTE NOT TO SHOW THEIR RESULTS BUT INCLUDE IN AVERAGE
        TS_PLUS = round(TS/average_ts * 100)
        player.append(name)
        player.append(TS*100)
        player.append(TS_PLUS)
        #if stats[0]==1:
        if True:
            data.append(player)
        #print(name,":", TS_PLUS)

        # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Name', 'True Shooting %','True Shooting+'])
    return df
    #print(average_ts)