#Count the total number of normal and tied matches. 

import pandas as pd

df=pd.read_csv(r'C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv')

normal_count=(df[df['result']=='normal']['result'].count())
tie_count=(df[df['result']=='tie']['result'].count())

print(f"Normal Matches: {normal_count}\nTied Matched: {tie_count}")