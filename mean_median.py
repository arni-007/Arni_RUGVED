#Calculate mean, median and standard deviation of ‘win_by_runs’ 

import pandas as pd

df=pd.read_csv(r'C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv')

mean=df['win_by_runs'].mean()
median=df['win_by_runs'].median()
standard_dev=df['win_by_runs'].std()

print(f"Mean: {mean}\nMedian: {median}\nStandard Deviation: {standard_dev}")
