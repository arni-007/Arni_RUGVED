#Find the cities where the maximum and minimum number of matches were conducted.

import pandas as pd

df= pd.read_csv(r'C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv')

city_counts=df['city'].value_counts()

print(city_counts)

max_city= city_counts.idxmax()
max_count=city_counts.max()

min_city=city_counts.idxmin()
min_count=city_counts.min()

print(f"City with maximum matches: {max_city} - {max_count}")
print(f"City with maximum matches: {min_city} - {min_count}")