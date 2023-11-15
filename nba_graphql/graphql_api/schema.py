import graphene
from graphene_django import DjangoObjectType
from .models import PlayerData


class PlayerDataType(DjangoObjectType):
    class Meta:
        model = PlayerData
        fields = "__all__"


class Query(graphene.ObjectType):
    all_players = graphene.List(
        PlayerDataType, first=graphene.Int(), skip=graphene.Int()
    )
    player = graphene.Field(PlayerDataType, name=graphene.String(required=True))

    def resolve_all_players(root, info, first=None, skip=None):
        players = PlayerData.objects.all()
        if first:
            players = players[:first]
        if skip:
            players = players[skip:]
        return players

    def resolve_player(root, info, name):
        try:
            return PlayerData.objects.get(name=name)
        except PlayerData.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)


