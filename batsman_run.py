#Calculate total number of runs scored by each batsman and display top 10.

import pandas as pd

df2=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\deliveries.csv")

runs= df2.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)

print(runs.head(10))