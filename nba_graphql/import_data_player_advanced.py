import os
import csv
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba_graphql.settings")
django.setup()

from graphql_api.models import PlayerDataAdvanced

# Obtain Player Advanced Data
season_input = input('What season? ')

try:
    season_int = int(season_input)
except ValueError:
    print('Invalid Value')
    exit(1)

url = 'https://www.basketball-reference.com/leagues/NBA_' + str(season_int) + '_advanced.html'
print(url)

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find advanced table
div = soup.find("div", {'id': 'all_advanced_stats'})
table = div.find("table", attrs={"id": "advanced_stats"})

# Extract headers
headers = table.find_all("th")
header_values = [th.text for th in headers][:29]
header_values.append('Player-additional')

# Test and view headers obtained.
'''
print(header_values, file=open("../data/advanced/header_values_advanced.txt", "w"))
'''

rows = table.find_all('tr')

data_rows = []

for row in rows:
    cols = row.find_all("td")
    th = row.find('th')
    rank = th.text if th else None
    cols = [rank] + [ele.text.strip() for ele in cols]
    player_id_col = row.find("td", attrs={'data-append-csv': True})
    if player_id_col:
        player_id = player_id_col['data-append-csv']
        cols.append(player_id)
        data_rows.append(cols)

# Write to CSV
with open(f'../data/advanced/{season_int}_player_advanced_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header_values)
    writer.writerows(data_rows)

print('Write to CSV success!')
