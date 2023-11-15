# Example Queries

```graphql
query MyQuery {
  allPlayers(first: 300, skip: 280) {
    PTS
    name
    team
    season
    threePercent
    age
  }
}

query MyQuery2 {
  player(name: "LeBron James", season: 2022, team: "LAL") {
    name
    season
    team
    games
    AST
    STL
    age
    effectFgPercent
    threeFg
    twoFg
    ftPercent
    BLK
    PTS
  }
}

query MyQuery3 {
  player(name: "James Harden", season: 2020) {
    name
    season
    team
    age
    PTS
  }
}
```

# Sample Response

```graphql
{
  "data": {
    "allPlayers": [
      {
        "PTS": "7.10",
        "name": "Ty Jerome",
        "team": "OKC",
        "season": 2022,
        "threePercent": "0.290",
        "age": 24
      },
      {
        "PTS": "5.30",
        "name": "Derrick Favors",
        "team": "OKC",
        "season": 2022,
        "threePercent": "0.125",
        "age": 30
      },
      {
        "PTS": "4.30",
        "name": "Mamadi Diakite",
        "team": "OKC",
        "season": 2022,
        "threePercent": "0.000",
        "age": 25
      }
    ]
  }
}
```

```graphql
{
  "data": {
    "player": {
      "name": "LeBron James",
      "season": 2022,
      "team": "LAL",
      "games": 56,
      "AST": "6.20",
      "STL": "1.30",
      "age": 37,
      "effectFgPercent": "0.590",
      "threeFg": "2.90",
      "twoFg": "8.60",
      "ftPercent": "0.756",
      "BLK": "1.10",
      "PTS": "30.30"
    }
  }
}
```

```graphql
{
  "data": {
    "player": {
      "name": "James Harden",
      "season": 2020,
      "team": "HOU",
      "age": 30,
      "PTS": "34.30"
    }
  }
}
```
