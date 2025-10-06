#Find the umpires who umpired the maximum number of times. 

import pandas as pd
import seaborn as sb 

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

season=df.groupby('season')[['season']].value_counts()

print(season)