WITH minRanks AS (
  SELECT
    minutes_pg,
    PERCENT_RANK() OVER (ORDER BY minutes_pg DESC) AS rank
  FROM
    graphql_api_playerdatatotalsplayoffs
  	
)
SELECT
  AVG(minutes_pg) AS AverageTop25Percent
FROM
  minRanks
WHERE
  rank <= 0.25;
  
---

SELECT *, (dt.total_rb/da.games) as calc, (dt.points/da.games) as ppg
FROM graphql_api_playerdatatotalsplayoffs dt
JOIN graphql_api_playerdataadvancedplayoffs da ON dt.player_id = da.player_id AND dt.season = da.season AND dt.team = da.team
WHERE
	dt.minutes_pg >= 476
  AND dt.player_id = 'onealsh01'




---

SELECT *
FROM graphql_api_playerdata
WHERE games >= 70
and points >= 17
and season = 2024


SELECT *
FROM graphql_api_playerdataadvanced
WHERE id in (SELECT id
FROM graphql_api_playerdata
WHERE games >= 70
and points >= 17
and season = 2024)






SELECT pt.id, pa.player_name, pa.position, pa.games, pa.per, pa.ts_percent, pa.turnover_percent, pa.usage_percent, pa.offensive_ws, pa.defensive_ws, pa.win_shares, pa.box, pa.offensive_box, pa.defensive_box, pt.blocks, pt.assists, pt.points, pt.season, pt.minutes_pg
FROM graphql_api_playerdataadvanced pa
JOIN graphql_api_playerdatatotals pt on pa.id = pt.id
WHERE pt.season = 2024
AND pt.minutes_pg >= 1985
ORDER BY pt.blocks DESC


SELECT pt.id, pa.player_name, pa.position, pa.games, pa.per, pa.ts_percent, pa.turnover_percent, pa.usage_percent, pa.offensive_ws, pa.defensive_ws, pa.win_shares, pa.box, pa.offensive_box, pa.defensive_box, pt.blocks, pt.assists, pt.points, pt.season
FROM graphql_api_playerdataadvanced pa
JOIN graphql_api_playerdatatotals pt on pa.id = pt.id
WHERE pt.blocks >= 144
ORDER BY pt.blocks DESC

SELECT pa.player_name, pa.position, pa.games, pa.usage_percent, pa.offensive_ws, pa.defensive_ws, pa.win_shares, pt.blocks,  pt.points, pt.season
FROM graphql_api_playerdataadvanced pa
JOIN graphql_api_playerdatatotals pt on pa.id = pt.id
WHERE pt.blocks >= 254
ORDER BY pt.blocks DESC

SELECT pa.player_name, pa.position, pa.games, pa.usage_percent, pa.offensive_ws, pa.defensive_ws, pa.win_shares, pt.blocks,  pt.points, pt.season
FROM graphql_api_playerdataadvanced pa
JOIN graphql_api_playerdatatotals pt on pa.id = pt.id
WHERE pt.blocks >= 254
ORDER BY pt.blocks DESC




---




