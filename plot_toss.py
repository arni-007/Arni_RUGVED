#Visualize toss decisions across all seasons

import pandas as pd
import matplotlib.pyplot as mypy

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

#field_dec= df.groupby('season')[df['toss_decision'=='field']]['toss_decision'].value_counts()
#bat_dec=df.groupby('season')[df['toss_decision'=='bat']]['toss_decision'].value_counts()

#field_dec.plot(kind='line',color='magenta',marker='^')

# bat_dec.plot(kind='line',color='orange',marker='^')

toss_counts = df.groupby(['season', 'toss_decision']).size().unstack(fill_value=0)

toss_counts.plot(kind='bar', color=['green', 'cyan'])

mypy.xlabel('Toss Decision')
mypy.ylabel('Number of Matches')
mypy.xticks(rotation=45)
mypy.title('Toss Decision')
mypy.show()