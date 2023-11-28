import graphene
from graphene_django import DjangoObjectType
from .models import PlayerData


class PlayerDataType(DjangoObjectType):
    class Meta:
        model = PlayerData
        fields = "__all__"


class Query(graphene.ObjectType):
    all_players = graphene.List(
        PlayerDataType, season=graphene.Int(required=True), first=graphene.Int(), skip=graphene.Int()
    )
    player = graphene.List(
        PlayerDataType,
        name=graphene.String(required=True),
        team=graphene.String(),
        season=graphene.Int(),
    )

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
