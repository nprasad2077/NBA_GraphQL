from django.db import models

# Create your models here.
class PlayerData(models.Model):
    player_name = models.CharField(max_length=255)
    position = models.CharField(max_length=30)
    age = models.IntegerField()
    games = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    minutes_pg = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    field_goals = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    field_attempts = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    field_percent = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    three_fg = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    three_attempts = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    three_percent = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    two_fg = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    two_attempts = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    two_percent = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    ft = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    ft_attempts = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    ft_percent = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    offensive_rb = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    defensive_rb = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    total_rb = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    assists = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    steals = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    blocks = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    turnovers = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    personal_fouls = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    points = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    player_id = models.CharField(max_length=255, primary_key=True)
    
    def __str__(self):
        return self.player_name