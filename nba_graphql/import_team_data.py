import os
import csv
import django
import requests
import re
from bs4 import BeautifulSoup
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba_graphql.settings")
django.setup()

from graphql_api.models import TeamData

# Obtain Team Data
team_search = input('What team? ')

try:
    team_abr = str(team_search)   
except ValueError:
    print('Invalid value')
    exit(1)

url = 'https://www.basketball-reference.com/teams/' + team_abr + '/'
print(url)

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Obtain Team Table
div = soup.find("div", {"id": "div_" + team_abr})
table = div.find("table", attrs={"id": team_abr})

headers = table.find_all("th")
header_values = [ele.text.replace('\xa0', ' ').strip() for ele in headers][:19]
header_values.append("top_ws_player")
header_values.append("ws")

# print(header_values)

# Extract rows into table.

# Extract rows into table.
rows = table.find_all("tr")

data_rows = []

for row in rows[2:]: # Skip first row and second
    cols = row.find_all("td")
    th = row.find('th')
    rank = th.text if th else None
     # Remove the 'Â' character and strip the text in the columns.
    cols = [ele.text.replace('\xa0', ' ').strip() for ele in cols] # Extract text from HTML element and remove any extra whitespace 
    
    # assuming 'Top WS' column is the last one before appending 'top_ws_player' and 'ws'
    top_ws_data = cols[-1] if cols else None  # get 'top_ws' data
    
    # initial 'top_ws_player' and 'ws' data as None
    top_ws_player = None
    ws = None
    
    # If 'top_ws' data is available then we will parse it
    if top_ws_data:
        match = re.match(r"(.*)\s\(([0-9.]*)\)", top_ws_data)
        top_ws_player = match.group(1) if match else None
        ws = match.group(2) if match else None

    # Append 'top_ws', 'top_ws_player', and 'ws' to cols
    # cols.append(top_ws_data)
    cols.append(top_ws_player)
    cols.append(ws)
    data_rows.append([rank] + cols)

# print(data_rows)

with open(f"../data/team/{team_search}.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header_values) # write headers
    writer.writerows(data_rows)

print('Write to CSV success')

def try_parse_float(s):
    try:
        return float(s)
    except ValueError:
        return None


def run():
    with open(f"../data/team/{team_abr}.csv", 'r') as file:
        reader = csv.DictReader(file)
        
        current_year = datetime.datetime.now().year
        
        for row in reader:
            team = TeamData()
            
            team.team_name = row['Team']
            team.team_abbr = team_abr
           # Split the season string
            season_year_part = row['Season'].split("-")[1]

            if int(season_year_part) <= current_year % 100:  # If the year part is less than or equal to current year's last 2 digits
                season_year = int("20" + season_year_part)  # prepend '20'
            else:
                season_year = int("19" + season_year_part)  # prepend '19'

            team.season = season_year
            team.league = row['Lg']
            
            team.wins = int(row['W']) if row['W'].isdigit() else None
            team.loss = int(row['L']) if row['L'].isdigit() else None
            
            team.win_loss_percent = try_parse_float(row['W/L%'])
            team.srs = try_parse_float(row['SRS'])
            
            team.finish = row['Finish']
            
            team.pace = try_parse_float(row['Pace'])
            team.rel_pace = try_parse_float(row['Rel Pace'])
            team.ortg = try_parse_float(row['ORtg'])
            team.rel_ortg = try_parse_float(row['Rel ORtg'])
            team.drtg = try_parse_float(row['DRtg'])
            team.rel_drtg = try_parse_float(row['Rel DRtg'])
            team.ws = try_parse_float(row['ws'])

            team.playoffs = row['Playoffs']
            team.coaches = row['Coaches']
            team.top_ws = row['Top WS']
            
            team.top_ws_player = row['top_ws_player']
            
            
            
            try:
                team.save()
                # print(team.__dict__)
            except Exception as e:
                print(f"Row Data: {row}")
                print(f'Could not create record: {e}')
                
run()

print('Write TeamData to DB Success!')