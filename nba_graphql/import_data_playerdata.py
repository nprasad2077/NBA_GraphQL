import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba_graphql.settings")
django.setup()

from graphql_api.models import PlayerData

season = input("What season? ")
season_int = int(season)

print(f"season is {season_int}")


def run():
    with open("../data/2023_season_per_game.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            player = PlayerData()
            player.player_name = row["Player"]
            player.position = row["Pos"]

            # Add the check for each field
            player.age = row["Age"] if row["Age"] else None
            player.games = row["G"] if row["G"] else None
            player.games_started = row["GS"] if row["GS"] else None
            player.minutes_pg = row["MP"] if row["MP"] else None
            player.field_goals = row["FG"] if row["FG"] else None
            player.field_attempts = row["FGA"] if row["FGA"] else None
            player.field_percent = row["FG%"] if row["FG%"] else None
            player.three_fg = row["3P"] if row["3P"] else None
            player.three_attempts = row["3PA"] if row["3PA"] else None
            player.three_percent = row["3P%"] if row["3P%"] else None
            player.two_fg = row["2P"] if row["2P"] else None
            player.two_attempts = row["2PA"] if row["2PA"] else None
            player.two_percent = row["2P%"] if row["2P%"] else None
            player.effect_fg_percent = row["eFG%"] if row["eFG%"] else None
            player.ft = row["FT"] if row["FT"] else None
            player.ft_attempts = row["FTA"] if row["FTA"] else None
            player.ft_percent = row["FT%"] if row["FT%"] else None
            player.offensive_rb = row["ORB"] if row["ORB"] else None
            player.defensive_rb = row["DRB"] if row["DRB"] else None
            player.total_rb = row["TRB"] if row["TRB"] else None
            player.assists = row["AST"] if row["AST"] else None
            player.steals = row["STL"] if row["STL"] else None
            player.blocks = row["BLK"] if row["BLK"] else None
            player.turnovers = row["TOV"] if row["TOV"] else None
            player.personal_fouls = row["PF"] if row["PF"] else None
            player.points = row["PTS"] if row["PTS"] else None
            player.team = row["Tm"] if row["Tm"] else None

            player.season = season_int
            player.player_id = row["Player-additional"]

            try:
                player.save()
            except Exception as e:
                print(f"Couldn't create record: {e}")


run()
print("success")
