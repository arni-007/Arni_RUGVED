#Find the umpires who umpired the maximum number of times. 

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

season=df.groupby('season')[['season']].value_counts().sort_values(ascending=False)

print(season)