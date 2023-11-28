from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class PlayerData(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    minutes_pg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_goals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    three_fg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    two_fg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    effect_fg_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    ft = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fta = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ft_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    ORB = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    DRB = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TRB = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    AST = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    STL = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    BLK = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TOV = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PF = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PTS = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    team = models.CharField(max_length=30, default="")
    season = models.IntegerField(null=True)

    class Meta:
        db_table = "nba_data_playerdata"
        managed = False

    def __str__(self):
        return self.name
    


class PlayerTotalsData(models.Model):
    player_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    minutes_played = models.IntegerField(null=True)
    field_goals = models.IntegerField(null=True)
    field_attempts = models.IntegerField(null=True)
    field_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    three_fg = models.IntegerField(null=True)
    three_attempts = models.IntegerField(null=True)
    three_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    two_fg = models.IntegerField(null=True)
    two_attempts = models.IntegerField(null=True)
    two_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    effect_fg_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    ft = models.IntegerField(null=True)
    fta = models.IntegerField(null=True)
    ft_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    ORB= models.IntegerField(null=True)
    DRB = models.IntegerField(null=True)
    TRB = models.IntegerField(null=True)
    AST = models.IntegerField(null=True)
    STL = models.IntegerField(null=True)
    BLK = models.IntegerField(null=True)
    TOV = models.IntegerField(null=True)
    PF = models.IntegerField(null=True)
    PTS = models.IntegerField(null=True)
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    
    class Meta:
        db_table = "nba_data_playertotalsdata"
        managed = False
    
    def __str__(self):
        return self.player_name
