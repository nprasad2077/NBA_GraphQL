import graphene
from graphene_django import DjangoObjectType
from .models import PlayerData, PlayerTotalsData


class PlayerDataType(DjangoObjectType):
    class Meta:
        model = PlayerData
        fields = (
            'name', 'age', 'games', 'games_started', 'minutes_pg', 'field_goals',
            'field_attempts', 'field_percent', 'three_fg', 'three_attempts',
            'three_percent', 'two_fg', 'two_attempts', 'two_percent',
            'effect_fg_percent', 'ft', 'fta', 'ft_percent', 'ORB', 'DRB',
            'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'team', 'season'
        )

class PlayerTotalsDataType(DjangoObjectType):
    class Meta:
        model = PlayerTotalsData
        fields = (
            'player_name', 'age', 'games', 'games_started', 'minutes_played',
            'field_goals', 'field_attempts', 'field_percent', 'three_fg',
            'three_attempts', 'three_percent', 'two_fg', 'two_attempts',
            'two_percent', 'effect_fg_percent', 'ft', 'fta', 'ft_percent',
            'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'team', 'season'
        )



class Query(graphene.ObjectType):
    all_players = graphene.List(
        PlayerDataType,
        season=graphene.Int(required=True),
        first=graphene.Int(),
        skip=graphene.Int(),
    )
    player = graphene.List(
        PlayerDataType,
        name=graphene.String(required=True),
        team=graphene.String(),
        season=graphene.Int(),
    )
    player_totals = graphene.List(
        PlayerTotalsDataType,
        player_name=graphene.String(required=True),
        team=graphene.String(),
        season=graphene.Int(),
    )
    
    def resolve_player_totals(root, info, player_name, team=None, season=None):
        query = PlayerTotalsData.objects.filter(player_name=player_name)
        if team:
            query = query.filter(team=team)
        if season:
            query = query.filter(season=season)
        return query

    def resolve_all_players(root, info, season, first=None, skip=None):
        players = PlayerData.objects.filter(season=season)
        if first:
            players = players[:first]
        if skip:
            players = players[skip:]
        return players

    def resolve_player(root, info, name, team=None, season=None):
        query = PlayerData.objects.filter(name=name)
        if team:
            query = query.filter(team=team)
        return query


schema = graphene.Schema(query=Query)
