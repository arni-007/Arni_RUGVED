#Find all deliveries where the batsman scored a six. 

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\deliveries.csv")

condition= df[df['batsman_runs']==6][['match_id','batsman']]

print(condition)