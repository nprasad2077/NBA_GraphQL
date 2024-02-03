import os
import csv
import django
import requests
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
