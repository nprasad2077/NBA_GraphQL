import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba_graphql.settings")
django.setup()

from graphql_api.models import PlayerData

season = input('What season? ')
season_int = int(season)

print(f'season is {season_int}')

def run():
    with open('../data/2023_season_per_game.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # player = PlayerData()
            print(row['Player'])

run()
