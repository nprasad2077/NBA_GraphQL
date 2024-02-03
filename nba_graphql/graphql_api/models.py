from django.db import models


# Create your models here.
class PlayerData(models.Model):
    player_name = models.CharField(max_length=255)
    position = models.CharField(max_length=30, default="")
    age = models.IntegerField(null=False)
    games = models.IntegerField(null=True, blank=True)
    games_started = models.IntegerField(null=True, blank=True)
    minutes_pg = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    field_goals = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True
    )
    field_attempts = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True
    )
    field_percent = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    three_fg = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    three_attempts = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    three_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    two_fg = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    two_attempts = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    two_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    effect_fg_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    ft = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    ft_attempts = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    ft_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    offensive_rb = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    defensive_rb = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    total_rb = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    assists = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    steals = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    blocks = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    turnovers = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    personal_fouls = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    points = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    team = models.CharField(max_length=30, default="")
    season = models.IntegerField(null=True)
    player_id = models.CharField(max_length=255)

    def __str__(self):
        return self.player_name


class PlayerDataTotals(models.Model):
    player_name = models.CharField(max_length=255)
    position = models.CharField(max_length=30, default="")
    age = models.IntegerField(null=False)
    games = models.IntegerField(null=True, blank=True)
    games_started = models.IntegerField(null=True, blank=True)
    minutes_pg = models.DecimalField(
        max_digits=5, decimal_places=1, null=True, blank=True
    )
    field_goals = models.IntegerField(null=True, blank=True)
    field_attempts = models.IntegerField(null=True, blank=True)
    field_percent = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    three_fg = models.IntegerField(null=True, blank=True)
    three_attempts = models.IntegerField(null=True, blank=True)
    three_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    two_fg = models.IntegerField(null=True, blank=True)
    two_attempts = models.IntegerField(null=True, blank=True)
    two_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    effect_fg_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    ft = models.IntegerField(null=True, blank=True)
    ft_attempts = models.IntegerField(null=True, blank=True)
    ft_percent = models.DecimalField(
        max_digits=4, decimal_places=3, null=True, blank=True
    )
    offensive_rb = models.IntegerField(null=True, blank=True)
    defensive_rb = models.IntegerField(null=True, blank=True)
    total_rb = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    steals = models.IntegerField(null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)
    turnovers = models.IntegerField(null=True, blank=True)
    personal_fouls = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    team = models.CharField(max_length=30, default="")
    season = models.IntegerField(null=True)
    player_id = models.CharField(max_length=255)

    def __str__(self):
        return self.player_name


class PlayerDataAdvanced(models.Model):
    player_name = models.CharField(max_length=255)
    position = models.CharField(max_length=30, default="")
    age = models.IntegerField(null=False)
    games = models.IntegerField(null=True, blank=True)
    minutes_played = models.IntegerField(null=True, blank=True)
    per = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    ts_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    three_p_ar = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    ftr = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    offensive_rb_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    defensive_rb_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    total_rb_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    assist_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    steal_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    block_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    turnover_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    usage_percent = models.DecimalField(
        max_digits=6, decimal_places=3, null=True, blank=True
    )
    offensive_ws = models.DecimalField(
        max_digits=5, decimal_places=1, null=True, blank=True
    )
    defensive_ws = models.DecimalField(
        max_digits=5, decimal_places=1, null=True, blank=True
    )
    win_shares = models.DecimalField(
        max_digits=5, decimal_places=1, null=True, blank=True
    )
    win_shares_per = models.DecimalField(
        max_digits=7, decimal_places=3, null=True, blank=True
    )
    offensive_box = models.DecimalField(
        max_digits=7, decimal_places=1, null=True, blank=True
    )
    defensive_box = models.DecimalField(
        max_digits=7, decimal_places=1, null=True, blank=True
    )
    box = models.DecimalField(max_digits=7, decimal_places=1, null=True, blank=True)
    vorp = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    team = models.CharField(max_length=30, default="")
    season = models.IntegerField(null=True)
    player_id = models.CharField(max_length=255)

    def __str__(self):
        return self.player_name
