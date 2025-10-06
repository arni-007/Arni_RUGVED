#Compute the average runs scored in matches in all the venues.

import pandas as pd

df=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\Matches.csv")
df2=pd.read_csv(r"C:\Users\Arni\OneDrive\Desktop\RUGVED\task2\deliveries.csv")

match_runs = df2.groupby('match_id')['total_runs'].sum().reset_index()
match_venue = df[['id', 'venue']].rename(columns={'id': 'match_id'})
match_runs_venue = pd.merge(match_runs, match_venue, on='match_id')

venue_avg = match_runs_venue.groupby('venue')['total_runs'].agg(['mean', 'count']).reset_index()
venue_avg = venue_avg.rename(columns={'mean': 'average_runs', 'count': 'matches_played'})

print(venue_avg)