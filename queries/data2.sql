WITH ScoreRanks AS (
  SELECT
    points,
    PERCENT_RANK() OVER (ORDER BY points DESC) AS rank
  FROM
    graphql_api_playerdatatotals
 	WHERE season = 2024
  	
)
SELECT
  AVG(points) AS AverageTop25Percent
FROM
  ScoreRanks
WHERE
  rank <= 0.25;
  
  
  WITH ScoreRanks AS (
  SELECT
    points,
    PERCENT_RANK() OVER (ORDER BY points DESC) AS rank
  FROM
    graphql_api_playerdata
  WHERE
    season = 2024
)
SELECT
  AVG(points) AS AverageTop25Percent
FROM
  ScoreRanks
WHERE
  rank <= 0.25;
  
  
  
  
WITH minRanks AS (
  SELECT
    minutes_pg,
    PERCENT_RANK() OVER (ORDER BY minutes_pg DESC) AS rank
  FROM
    graphql_api_playerdatatotals
 	WHERE season = 2024
  	
)
SELECT
  AVG(minutes_pg) AS AverageTop25Percent
FROM
  minRanks
WHERE
  rank <= 0.30;
  
  

WITH threeRanks AS (
  SELECT
    three_attempts,
    PERCENT_RANK() OVER (ORDER BY three_attempts DESC) AS rank
  FROM
    graphql_api_playerdatatotalsplayoffs
 	WHERE season = 2024
  	
)
SELECT
  AVG(three_attempts) AS AverageTop25Percent
FROM
  threeRanks
WHERE
  rank <= 0.25;
  
  
 WITH GameRanks AS (
  SELECT
   games,
    PERCENT_RANK() OVER (ORDER BY games DESC) AS rank
  FROM
    graphql_api_playerdata
  WHERE
    season = 2024
)
SELECT
  AVG(games) AS AverageTop25Percent
FROM
  GameRanks
WHERE
  rank <= 0.25;



 WITH GameRanks AS (
  SELECT
   games,
    PERCENT_RANK() OVER (ORDER BY games DESC) AS rank
  FROM
    graphql_api_playerdata
  WHERE
    season = 2024
  and points >= 17
)
SELECT
  AVG(games) AS AverageTop25Percent
FROM
  GameRanks
WHERE
  rank <= 0.25;



  WITH ScoreRanks AS (
  SELECT
    points,
    PERCENT_RANK() OVER (ORDER BY points DESC) AS rank
  FROM
    graphql_api_playerdatatotals
  WHERE
    season = 2024
)
SELECT
  AVG(points) AS AverageTop25Percent
FROM
  ScoreRanks
WHERE
  rank <= 0.25;
