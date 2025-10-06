#Find the team which won the match by the highest and lowest number of runs

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

high_run=df[df['win_by_runs']>0]['win_by_runs'].max()
low_run=df[df['win_by_runs']>0]['win_by_runs'].min()

max_win_team= df[df['win_by_runs']==high_run]['winner'].unique()
min_win_team= df[df['win_by_runs']==low_run]['winner'].unique()

print(f"Highest: {', '.join(max_win_team)} won by {high_run} runs\nLowest: {', '.join(min_win_team)} won by {low_run} runs")


