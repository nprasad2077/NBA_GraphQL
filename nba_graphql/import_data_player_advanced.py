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

# Write to Database

def run():
    with open(f'../data/advanced/{season_int}_player_advanced_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            player = PlayerDataAdvanced()
            player.player_name = row['Player']
            player.position = row['Pos']
            
            # Data with check
            player.age = row['Age'] if row['Age'] else None
            player.games = row['G'] if row['G'] else None
            player.minutes_played = row['MP'] if row['MP'] else None
            player.per = row['PER'] if row['PER'] else None
            player.ts_percent = row['TS%'] if row['TS%'] else None
            player.three_p_ar = row['3PAr'] if row['3PAr'] else None
            player.ftr = row['FTr'] if row['FTr'] else None
            player.offensive_rb_percent = row['ORB%'] if row['ORB%'] else None
            player.defensive_rb_percent = row['DRB%'] if row['DRB%'] else None
            player.total_rb_percent = row['TRB%'] if row['TRB%'] else None
            player.assist_percent = row['AST%'] if row['AST%'] else None
            player.steal_percent = row['STL%'] if row['STL%'] else None
            player.block_percent = row['BLK%'] if row['BLK%'] else None
            player.turnover_percent = row['TOV%'] if row['TOV%'] else None
            player.usage_percent = row['USG%'] if row['USG%'] else None
            player.offensive_ws = row['OWS'] if row['OWS'] else None
            player.defensive_ws = row['DWS'] if row['DWS'] else None
            player.win_shares = row['WS'] if row['WS'] else None
            player.win_shares_per = row['WS/48'] if row['WS/48'] else None
            player.offensive_box = row['OBPM'] if row['OBPM'] else None
            player.defensive_box = row['DBPM'] if row['DBPM'] else None
            player.box = row['BPM'] if row['BPM'] else None
            player.vorp = row['VORP'] if row['VORP'] else None
            
            
            
            player.team = row['Tm'] if row['Tm'] else None
            player.season = season_int
            player.player_id = row['Player-additional']
            
            try:
                player.save()
            except Exception as e:
                print(f'Row data: {row}')
                print(f'Could not create record {e}')
                
run()

print('Save to player advanced DB Success!')