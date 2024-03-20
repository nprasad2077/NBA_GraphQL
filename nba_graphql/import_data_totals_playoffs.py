import os
import django
import csv
import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba_graphql.settings")
django.setup()

from graphql_api.models import PlayerDataTotalsPlayoffs

# Get the website content
season_input = input('What season? ')
try:
    season_int = int(season_input)
except ValueError: 
    print('Invalid Value')
    exit(1)

url = "https://www.basketball-reference.com/playoffs/NBA_" + str(season_int) + "_totals.html"
print(url)

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# print(soup) # Add this line to check the entire HTML fetched

# Find the div with id `div_totals_stats`, then find the preformatted text within it
div = soup.find("div", {"id": "div_totals_stats"})
table = div.find("table", attrs={"id": "totals_stats"})

# Extract Headers and append player_id column.
headers = table.find_all("th")
header_values = [th.text for th in headers][:30]
header_values.append("Player-additional")
# header_values.append("season")


# Testing output

# print(div, file=open("div.txt", "w"))

# print(table, file=open("table.txt", "w"))

# print(header_values, file=open("headers.txt", "w"))

# Extract rows into table.

rows = table.find_all("tr")

data_rows = []

for row in rows:
    cols = row.find_all("td")
    th = row.find('th')
    rank = th.text if th else None
    cols = [rank] + [ele.text.strip() for ele in cols] # ele - Extract text from HTML element and strip() to remove any extra whitespace
    player_id_col = row.find("td", attrs={"data-append-csv": True})
    if player_id_col:
        player_id = player_id_col["data-append-csv"]
        cols.append(player_id)
        # cols.append(season_int)
        data_rows.append(cols)


# Write to CSV
with open(f"../data/totals_playoffs/{season_input}_player_totals_playoffs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header_values) # write headers
    writer.writerows(data_rows)

print('Write to CSV success')


# Write to Database

def run():
    with open(f"../data/totals_playoffs/{season_input}_player_totals_playoffs.csv", 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            player =  PlayerDataTotalsPlayoffs()
            player.player_name = row['Player']
            player.position = row['Pos']
            
            # Data with check
            player.age = row['Age'] if row['Age'] else None
            player.games = row['G'] if row['G'] else None
            player.games_started = row['GS'] if row['GS'] else None
            player.minutes_pg = row['MP'] if row['MP'] else None
            player.field_goals = row['FG'] if row['FG'] else None
            player.field_attempts = row['FGA'] if row['FGA'] else None
            player.field_percent = row['FG%'] if row ['FG%'] else None
            player.three_fg = row['3P'] if row['3P'] else None
            player.three_attempts = row['3PA'] if row['3PA'] else None
            player.three_percent = row['3P%'] if row['3P%'] else None
            player.two_fg = row['2P'] if row['2P'] else None
            player.two_attempts = row['2PA'] if row['2PA'] else None
            player.two_percent = row['2P%'] if row['2P%'] else None
            player.effect_fg_percent = row['eFG%'] if row['eFG%'] else None
            player.ft = row['FT'] if row['FT'] else None
            player.ft_attempts = row['FTA'] if row['FTA'] else None
            player.ft_percent = row['FT%'] if row['FT%'] else None
            player.offensive_rb =  row['ORB'] if row['ORB'] else None
            player.defensive_rb = row['DRB'] if row['DRB'] else None
            player.total_rb = row['TRB'] if row['TRB'] else None
            player.assists = row['AST'] if row['AST'] else None
            player.steals = row['STL'] if row['STL'] else None
            player.blocks = row['BLK'] if row['BLK'] else None
            player.turnovers = row['TOV'] if row['TOV'] else None
            player.personal_fouls = row['PF'] if row['PF'] else None
            player.points = row['PTS'] if row['PTS'] else None
            player.team = row['Tm'] if row['Tm'] else None
            
            player.season = season_int
            player.player_id = row['Player-additional']
            
            try:
                player.save()
            except Exception as e:
                print(f'Row data: {row}')
                print(f'Could not create record: {e}')

run()

print('Save to DB Success!')