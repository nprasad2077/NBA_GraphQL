import pandas as pd

# Load CSV files to compare

df1 = pd.read_csv('../data/totals/2023_player_totals.csv')
df2 = pd.read_csv('../data/totals/players.csv')

# Compare differences

diff = df1.compare(df2)
print(diff)

