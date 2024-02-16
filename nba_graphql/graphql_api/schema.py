import graphene
from graphene_django.types import DjangoObjectType
from .models import PlayerData, PlayerDataTotals, PlayerDataAdvanced, TeamData


class PlayerType(DjangoObjectType):
    class Meta:
        model = PlayerData

class PlayerTotalsType(DjangoObjectType):
    class Meta:
        model = PlayerDataTotals

class PlayerAdvancedType(DjangoObjectType):
    class Meta:
        model = PlayerDataAdvanced
        
class TeamDataType(DjangoObjectType):
    class Meta:
        model = TeamData


class Query(graphene.ObjectType):
    
    
    # Search for Team information
    team_by_name = graphene.List(
        TeamDataType,
        abbr=graphene.String(required=True),
        season=graphene.Int(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
     )
    
    player_per_game = graphene.List(
        PlayerType,
        name=graphene.String(),
        position=graphene.String(),
        age=graphene.Int(),
        games=graphene.Int(),
        games_started=graphene.Int(),
        minutes_pg = graphene.Decimal(),
        field_goals = graphene.Decimal(),
        field_attempts = graphene.Decimal(),
        field_percent = graphene.Decimal(),
        three_fg=graphene.Decimal(),
        three_attempts=graphene.Decimal(),
        three_percent=graphene.Decimal(),
        two_fg=graphene.Decimal(),
        two_attempts=graphene.Decimal(),
        two_percent=graphene.Decimal(),
        effect_fg_percent=graphene.Decimal(),
        ft=graphene.Decimal(),
        ft_attempts=graphene.Decimal(),
        orb=graphene.Decimal(),
        drb=graphene.Decimal(),
        trb=graphene.Decimal(),
        assists=graphene.Decimal(),
        steals=graphene.Decimal(),
        turnovers=graphene.Decimal(),
        personal_fouls=graphene.Decimal(),
        points=graphene.Decimal(),
        team=graphene.String(),
        player_id=graphene.String(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
        id=graphene.Int(),
    )
    
    player_totals = graphene.List(
        PlayerTotalsType,
        name=graphene.String(),
        position=graphene.String(),
        team=graphene.String(),
        season=graphene.Int(),
        player_id=graphene.String(),
        id=graphene.Int(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
    )
    
    player_advanced = graphene.List(
        PlayerAdvancedType,
        name=graphene.String(),
        position=graphene.String(),
        team=graphene.String(),
        season=graphene.Int(),
        player_id=graphene.String(),
        id=graphene.Int(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
    )
    
    player_totals_all = graphene.List(
        PlayerTotalsType,
        name=graphene.String(),
        position=graphene.String(),
        team=graphene.String(),
        season=graphene.Int(),
        player_id=graphene.String(),
        id=graphene.Int(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
    )
    
    player_advanced_all = graphene.List(
        PlayerAdvancedType,
        name=graphene.String(),
        position=graphene.String(),
        team=graphene.String(),
        season=graphene.Int(),
        player_id=graphene.String(),
        id=graphene.Int(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
    )
    
    player_per_game_all = graphene.List(
        PlayerType,
        name=graphene.String(),
        position=graphene.String(),
        team=graphene.String(),
        season=graphene.Int(),
        player_id=graphene.String(),
        id=graphene.Int(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
    )
          
    def resolve_team_by_name(self, info, abbr, season=None, ordering=None, first=None, limit=None, **kwargs):
        t = TeamData.objects.filter(team_abbr=abbr)
        
        if season:
            t = t.filter(season=season)
            
        if ordering:
            t = t.order_by(ordering)
        
        if first:
            t = t[first:limit]
        
        if limit:
            t = t[first:limit]
            
    def resolve_player_per_game(self, info, name=None, season=None, player_id=None, team=None, position=None, age=None, id=None, ordering=None, first=None, limit=None, **kwargs ):
        
        if not name and not player_id and not id and not team and not position and not season:
            raise Exception('Either name, id, player_id, team, season, or position must be provided.')
        
        p = PlayerData.objects.all()
        
        if name:
            p = p.filter(player_name__icontains=name)
        
        if season:
            p = p.filter(season=season)
            
        if player_id:
            p = p.filter(player_id=player_id)
        
        if team:
            p = p.filter(team=team)
        
        if position:
            p = p.filter(position=position)
        
        if age:
            p = p.filter(age=age)
            
        if id:
            p = p.filter(id=id)
        
        if ordering:
            p = p.order_by(ordering)
        
        if first:
            p = p[first:limit]
        
        if limit:
            p = p[first:limit]
        
        return p
    
    def resolve_player_totals(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        
        if not name and not player_id and not id and not team and not position and not season:
            raise Exception('Either name, id, player_id, team, season, or position must be provided.')
        
        p = PlayerDataTotals.objects.all()
        
        if name:
            p = p.filter(player_name__icontains=name)
            
        if season:
            p = p.filter(season=season)
        
        if player_id:
            p = p.filter(player_id=player_id)
            
        if team:
            p = p.filter(team=team)
        
        if position:
            p = p.filter(position=position)
        
        if id:
            p = p.filter(id=id)
        
        if ordering:
            p = p.order_by(ordering)
        
        if first:
            p = p[first:limit]
        
        if limit:
            p = p[first:limit]
        
        return p
    
    def resolve_player_advanced(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        
        if not name and not player_id and not id and not season and not team and not position:
            raise Exception('Either name, id, player_id, team, season, or position must be provided.')
        
        p = PlayerDataAdvanced.objects.all()
        
        if name:
            p = p.filter(player_name__icontains=name)
        
        if season:
            p = p.filter(season=season)
        
        if player_id:
            p = p.filter(player_id=player_id)
        
        if team:
            p = p.filter(team=team)
        
        if position:
            p = p.filter(position=position)
        
        if id:
            p = p.filter(id=id)
        
        if ordering:
            p = p.order_by(ordering)
        
        if first:
            p = p[first:limit]
        
        if limit:
            p = p[first:limit]
        
        return p
    
    # New and Improved Queries will make all params optional for filtering.
    
    def resolve_player_totals_all(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        
        t = PlayerDataTotals.objects.all()
        
        if name:
            t = t.filter(player_name__icontains=name)
        
        if season:
            t = t.filter(season=season)
        
        if player_id:
            t = t.filter(player_id=player_id)
            
        if team:
            t = t.filter(team=team)
            
        if position:
            t = t.filter(position=position)
            
        if id:
            t = t.filter(id=id)
            
        if ordering:
            t = t.order_by(ordering)
        
        if first:
            t = t[first:limit]
        
        if limit:
            t = t[first:limit]
        
        return t


    def resolve_player_advanced_all(self, info,  name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        
        a = PlayerDataAdvanced.objects.all()
        
        if name:
            a = a.filter(player_name__icontains=name)
        
        if season:
            a = a.filter(season=season)
        
        if player_id:
            a = a.filter(player_id=player_id)
            
        if team:
            a = a.filter(team=team)
        
        if position:
            a = a.filter(position=position)
        
        if id:
            a = a.filter(id=id)
        
        if ordering:
            a = a.order_by(ordering)
            
        if first:
            a = a[first:limit]
            
        if limit:
            a = a[first:limit]
            
        return a
    
    
    def resolve_player_per_game_all(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        
        p = PlayerData.objects.all()
        
        if name:
            p = p.filter(player_name__icontains=name)
        
        if season:
            p = p.filter(season=season)
        
        if player_id:
            p = p.filter(id=id)
        
        if team:
            p = p.filter(team=team)
        
        if position:
            p = p.filter(position=position)
        
        if id:
            p = p.filter(id=id)
        
        if ordering:
            p = p.order_by(ordering)
        
        if first:
            p = p[first:limit]
            
        if limit:
            p = p[first:limit]
        
        return p
            
        
        
        
        