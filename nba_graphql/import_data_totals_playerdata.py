import os
import django
import csv
import requests
from bs4 import BeautifulSoup

# Get the website content
url = "https://www.basketball-reference.com/leagues/NBA_2023_totals.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup) # Add this line to check the entire HTML fetched

# Find the div with id `div_totals_stats`, then find the preformatted text within it
div = soup.find("div", {"id": "div_totals_stats"})
table = div.find("table", attrs={"id": "totals_stats"})

headers = table.find_all('th')
header_values = [th.text for th in headers][:30]
header_values.append('Player-additional')


# print(table)

print(div, file=open("div.txt", "w")) 

print(table, file=open("table.txt", "w"))

print(header_values, file=open("headers.txt", "w"))

