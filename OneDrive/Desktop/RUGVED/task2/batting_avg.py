#Compute batting averages and display top 10.

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")
df2=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\deliveries.csv")

total_runs = df2.groupby('batsman')['batsman_runs'].sum()

dismissals = df2[df2['player_dismissed'].notnull()].groupby('player_dismissed')['player_dismissed'].count()

batting_avg = (total_runs / dismissals).dropna().sort_values(ascending=False)

print(batting_avg.head(10))