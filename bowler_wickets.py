#Compute the total number of wickets taken by each bowler. 

import pandas as pd

df2=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\deliveries.csv")

wicket = df2[df2['player_dismissed'].notnull()].groupby('bowler')['player_dismissed'].count().sort_values(ascending=False)

print(wicket)

