#Find total runs scored in each season. 

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")
df2=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\deliveries.csv")

merged = pd.merge(df2[['match_id','total_runs']], df[['id', 'season']], left_on='match_id', right_on='id')

total_run= merged.groupby('season')[['season']].sum()

print(total_run)