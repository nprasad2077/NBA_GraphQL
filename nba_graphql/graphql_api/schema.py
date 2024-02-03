import graphene
from graphene_django.types import DjangoObjectType
from .models import PlayerData


class PlayerType(DjangoObjectType):
    class Meta:
        model = PlayerData


class Query(graphene.ObjectType):
    # Search for all players in a season. All paramaters available for viewing, just specify season.
    players_by_season = graphene.List(
        PlayerType,
        season=graphene.Int(required=True),
        team=graphene.String(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
    )

    # Search for player by Name. You may further refine your results with optional season and team parameters after specifying player name.
    player_by_name = graphene.List(
        PlayerType,
        name=graphene.String(required=True),
        season=graphene.Int(),
        team=graphene.String(),
        ordering=graphene.String(),
        limit=graphene.Int(),
    )

    # Search for team roster by abbreviation. Filter additionally by season.
    players_by_team = graphene.List(
        PlayerType,
        team=graphene.String(required=True),
        season=graphene.Int(),
        position=graphene.String(),
        ordering=graphene.String(),
    )

    def resolve_players_by_season(
        self, info, season, team=None, ordering=None, limit=None, first=None, **kwargs
    ):
        q = PlayerData.objects.filter(season=season)
        
        if team:
            q = q.filter(team=team)

        if ordering:
            q = q.order_by(ordering)
        
        if first:
            q = q[first:limit]

        if limit:
            q = q[first:limit]

        return q

    def resolve_player_by_name(self, info, name, season=None, team=None, ordering=None, limit=None, **kwargs):
        search = PlayerData.objects.filter(player_name=name)

        if season:
            search = search.filter(season=season)

        if team:
            search = search.filter(team=team)
        
        if ordering:
            search = search.order_by(ordering)
            
        if limit:
            search = search[:limit]

        return search

    def resolve_players_by_team(self, info, team, season=None, position=None, ordering=None, **kwargs):
        p = PlayerData.objects.filter(team=team)

        if season:
            p = p.filter(season=season)

        if position:
            p = p.filter(position=position)
        
        if ordering:
            p = p.order_by(ordering)

        return p
