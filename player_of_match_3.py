#Find the players who have won ‘Player of the Match’ more than 3 times. 

import pandas as pd

df= pd.read_csv(r'C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv')

name=df['player_of_match'].value_counts()

print(name)

condition=name[name>3].index.tolist()

print(f"The players who have won 'Player of the Match' more than 3 times are {', '.join(condition)}")