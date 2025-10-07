import pandas as pd

df= pd.read_csv(r'C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv')

ndf=df[(df['season']==2008)]

count= ndf.shape[0]

print(f"The number of matches in 2008 were {count}")