import graphene
from graphene_django.types import DjangoObjectType
from .models import PlayerData, PlayerDataTotals, PlayerDataAdvanced, TeamData, PlayerDataTotalsPlayoffs, PlayerDataAdvancedPlayoffs, ShotChartData


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
        
class PlayerTotalsPlayoffsType(DjangoObjectType):
    class Meta:
        model = PlayerDataTotalsPlayoffs

class PlayerAdvancedPlayoffsType(DjangoObjectType):
    class Meta:
        model = PlayerDataAdvancedPlayoffs
        
class ShotChartType(DjangoObjectType):
    class Meta:
        model = ShotChartData

class Query(graphene.ObjectType):
    
    
    # Search for Team information
    team = graphene.List(
        TeamDataType,
        team_abbr=graphene.String(),
        team_name=graphene.String(),
        season=graphene.Int(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int(),
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
    
    player_per_game = graphene.List(
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
    
    player_totals_playoffs = graphene.List(
        PlayerTotalsPlayoffsType,
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
    
    player_advanced_playoffs = graphene.List(
        PlayerAdvancedPlayoffsType,
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
    
    shot_chart_data = graphene.List(
        ShotChartType,
        name=graphene.String(),
        date=graphene.String(),
        quarter=graphene.String(),
        time_remaining=graphene.String(),
        shot_type=graphene.String(),
        distance=graphene.Int(),
        lead=graphene.Boolean(),
        team=graphene.String(),
        season=graphene.Int(),
        player_id=graphene.String(),
        ordering=graphene.String(),
        first=graphene.Int(),
        limit=graphene.Int()
    )
    
          
    def resolve_team(self, info, team_abbr=None, team_name=None, season=None, ordering=None, first=None, limit=None, **kwargs):
        t = TeamData.objects.all()
        
        if team_abbr:
            t = t.filter(team_abbr=team_abbr)
            
        if team_name:
            t = t.filter(team_name__icontains=team_name)
            
        if season:
            t = t.filter(season=season)
            
        if ordering:
            t = t.order_by(ordering)
        
        if first:
            t = t[first:limit]
        
        if limit:
            t = t[first:limit]
        
        return t
            
    
    def resolve_player_totals(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        
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
    
    
    def resolve_player_per_game(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        
        
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
            
        
        
        
    def resolve_player_totals_playoffs(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        t =PlayerDataTotalsPlayoffs.objects.all()
        
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
            
        
    def resolve_player_advanced_playoffs(self, info, name=None, season=None, player_id=None, team=None, position=None, id=None, ordering=None, first=None, limit=None, **kwargs):
        a = PlayerDataAdvancedPlayoffs.objects.all()
        
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
    
    def resolve_shot_chart_data(self, info, name=None, player_id=None, team=None, date=None, quarter=None, time_remaining=None, shot_type=None, distance=None, lead=None, season=None, ordering=None, first=None, limit=None, **kwargs):
        s = ShotChartData.objects.all()
        
        if name:
            s = s.filter(player_name__icontains=name)
        
        if player_id: 
            s = s.filter(player_id=player_id)
        
        if team: 
            s = s.filter(team=team)
        
        if date:
            s = s.filter(date__icontains=date)
        
        if quarter:
            s = s.filter(qtr__icontains=quarter)
        
        if shot_type:
            s = s.filter(shot_type=shot_type)
        
        if distance:
            s = s.filter(distance>=distance)
        
        if lead:
            s = s.filter(lead=lead)
            
        if season:
            s = s.filter(season=season)
        
        if ordering: 
            s = s.order_by(ordering)
        
        if first:
            s = s[first:limit]
        
        if limit:
            s = s[first:limit]
        
        return s