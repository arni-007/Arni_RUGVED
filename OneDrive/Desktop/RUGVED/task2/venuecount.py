#Find the venue where the team won by the highest and lowest number of runs

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

high_run=df[df['win_by_runs']>0]['win_by_runs'].max()
low_run=df[df['win_by_runs']>0]['win_by_runs'].min()

max_win= df[df['win_by_runs']==high_run]['venue'].unique()
min_win= df[df['win_by_runs']==low_run]['venue'].unique()

print(f"Highest: {', '.join(max_win)}- {high_run} runs\nLowest: {', '.join(min_win)}- {low_run} run/runs")
