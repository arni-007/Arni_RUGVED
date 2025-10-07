import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")

city_count=df['city'].value_counts()
df.head(10)
print(city_count.head(5))