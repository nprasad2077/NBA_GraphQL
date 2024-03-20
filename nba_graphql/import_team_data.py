import os
import csv
import django
import requests
import re
from bs4 import BeautifulSoup

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

for row in rows[1:]: # Skip first row
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