import os
import django
import csv
import re
import requests
from bs4 import BeautifulSoup, Comment
from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba_graphql.settings")
django.setup()

from graphql_api.models import ShotChartData

# Obtain start and finish seasons from the user
start_season_input = input('Enter recent start season (e.g., 2016): ')
finish_season_input = input('Enter rookie finish season (e.g., 1997): ')

try:
    start_season = int(start_season_input)
    finish_season = int(finish_season_input)
    if start_season < finish_season:
        raise ValueError("Start season should be more recent than finish season.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

player_name = 'Stephen Curry'

# Function to get player ID
def get_player_id(name):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT player_name, player_id
            FROM graphql_api_playerdata
            WHERE player_name LIKE %s
        """, [f'%{name}%'])
        row = cursor.fetchone()
        return row[1] if row else None

player_id = get_player_id(player_name)
if not player_id:
    print(f"Player ID for {player_name} not found.")
    exit(1)

# Loop through each season in the specified range
for season in range(start_season, finish_season - 1, -1):
    url = f'https://www.basketball-reference.com/players/{player_id[:1]}/{player_id}/shooting/{season}'

    print(f"Fetching data for {player_name} for the {season} season.")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the comment containing the shot chart
    comment = soup.find(string=lambda text: isinstance(text, Comment) and "div_shot-chart" in text)
    shot_chart_soup = BeautifulSoup(comment, "html.parser")
    shot_chart = shot_chart_soup.find("div", {"id": "shot-wrapper"})
    shots = shot_chart.find_all("div", {"class": ["tooltip make", "tooltip miss"]})

    shot_chart_data = []

    for shot_div in shots:
        style_values = shot_div['style'].split(';')
        top_value = int(style_values[0].split(':')[1].replace('px', '').strip())
        left_value = int(style_values[1].split(':')[1].replace('px', '').strip())

        tip_parts = shot_div['tip'].split('<br>')
        date_and_opponent = re.split(' at | vs ', tip_parts[0])
        date = date_and_opponent[0].strip().split(',')[0] + ',' + date_and_opponent[0].strip().split(',')[1]
        team = date_and_opponent[0].strip().split(',')[2].strip()
        opponent = date_and_opponent[1].strip()

        quarter_and_time = tip_parts[1].split(',')
        quarter = quarter_and_time[0].strip()
        time_remaining = quarter_and_time[1].strip().split(' ')[0]

        result_and_type_and_distance = tip_parts[2].split(' ')
        result = result_and_type_and_distance[0].strip() == 'Made'
        shot_type = int(result_and_type_and_distance[1][0])        
        distance_ft = int(result_and_type_and_distance[-2].strip())

        team_score_and_opponent_score = tip_parts[3].split(' ')[-1].split('-')
        team_score = int(team_score_and_opponent_score[0].strip())
        opponent_score = int(team_score_and_opponent_score[1].strip())

        lead = team_score > opponent_score

        shot_chart_row = {
            'player_name': player_name,
            'top': top_value,
            'left': left_value,
            'date': date,
            'qtr': quarter,
            'time_remaining': time_remaining,
            'result': result,
            'shot_type': shot_type,
            'distance_ft': distance_ft,
            'lead': lead,
            'team_score': team_score,
            'opponent_team_score': opponent_score,
            'opponent': opponent,
            'team': team,
            'season': season,
            'player_id': player_id
        }
        shot_chart_data.append(shot_chart_row)

    # Writing to CSV
    csv_file_path = f"../data/shot_chart/{player_name}_{season}_shot_chart_data.csv"
    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=shot_chart_data[0].keys())
        writer.writeheader()
        for row in shot_chart_data:
            writer.writerow(row)

    print(f'Write to CSV success for season {season}')

    # Inserting into database
    try:
        ShotChartData.objects.bulk_create(
            ShotChartData(**row) for row in shot_chart_data
        )
    except Exception as e:
        print(f"Error inserting data into database for season {season}: {e}")

    print(f'Save to DB Success for season {season}!')
