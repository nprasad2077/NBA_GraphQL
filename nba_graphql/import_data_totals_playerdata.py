import os
import django
import csv
import requests
from bs4 import BeautifulSoup

# Get the website content
season_input = input('What season? ')
try:
    season_int = int(season_input)
except ValueError: 
    print('Invalid Value')
    exit(1)

url = "https://www.basketball-reference.com/leagues/NBA_" + str(season_int) + "_totals.html"
print(url)
url_print = 'https://www.basketball-reference.com/leagues/NBA_2023_totals.html'
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
header_values.append("season")


# Testing output

print(div, file=open("div.txt", "w"))

print(table, file=open("table.txt", "w"))

print(header_values, file=open("headers.txt", "w"))

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
        cols.append(season_int)
        data_rows.append(cols)


# Write to CSV

with open(f"../data/totals/{season_input}_player_totals.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header_values) # write headers
    writer.writerows(data_rows)


print('success')
