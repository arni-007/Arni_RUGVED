#Tally the toss decisions each team has taken

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")


toss_counts = df.groupby(['toss_winner', 'toss_decision']).size().reset_index(name='count')

print(toss_counts)
