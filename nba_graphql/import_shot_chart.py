import os
import django
import csv
import re
import requests
from bs4 import BeautifulSoup
from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba_graphql.settings")
django.setup()

from graphql_api.models import ShotChartData


season_input = input('What season? ')
try:
    season_int = int(season_input)
except ValueError: 
    print('Invalid Value')
    exit(1)

player_name = 'Kobe Bryant'

# Obtain PLayer_ID
def get_player_id(player_name):
    with connection.cursor() as cursor:
       cursor.execute("""
            SELECT DISTINCT player_name, player_id
            FROM graphql_api_playerdata
            WHERE player_name LIKE %s
        """, [f'%{player_name}%'])
       row = cursor.fetchone()
       return row[1]


player_id = get_player_id(player_name)

url = 'https://www.basketball-reference.com/players/' + player_id[:1] + '/' + player_id + '/shooting/' + season_input

print(url)
   


# Get Content

