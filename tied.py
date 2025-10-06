#Find the teams where the result was a tie. 

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

tied=df[df['result']=='tie'][['id','season','date','team1','team2']]

print(f"The teams whose matches ended with tie are as follow:\n{tied}")