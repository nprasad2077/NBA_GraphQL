import graphene
from graphene_django.types import DjangoObjectType
from .models import PlayerData

class PlayerType(DjangoObjectType):
    class Meta:
        model = PlayerData
        
class Query(graphene.ObjectType):
    player_by_season = graphene.List(PlayerType, season=graphene.Int(required=True))
    
    def resolve_players_by_season(self, info, season, **kwargs):
        return PlayerData.objects.filter(season=season)
    
    