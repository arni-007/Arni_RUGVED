#Find the umpires who umpired the maximum number of times

import pandas as pd 

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

umpires = pd.concat([df['umpire1'], df['umpire2'], df['umpire3']]).dropna()

umpire_counts = umpires.value_counts()

#max_count = umpire_counts.max()
#ax_umpires = umpire_counts[umpire_counts == max_count]


print("Umpires who umpired the maximum number of times:")

print(umpire_counts.head(5))