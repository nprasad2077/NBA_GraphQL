# GraphQL Query Examples

```graphQL
query allPlayersInASeason {
  allPlayers(season: 2020, first: 3, skip: 0, team: "HOU") {
    name
    age
    games
    gamesStarted
    minutesPg
    fieldGoals
    fieldAttempts
    fieldPercent
    threeFg
    threeAttempts
    threePercent
    twoFg
    twoAttempts
    twoPercent
    effectFgPercent
    ft
    fta
    ftPercent
    ORB
    DRB
    TRB
    AST
    STL
    BLK
    TOV
    PF
    PTS
    season
    team
  }
}
```

```graphQL
query OnePlayer {
  player(name: "LeBron James", season: 2015) {
    name
    PTS
    minutesPg
    team
    threePercent
    twoPercent
    ftPercent
    fieldPercent
    age
    AST
    BLK
    TRB
    season
  }
}
```

```graphQL

query singlePlayerTotals {
  playerTotals(playerName: "James Harden") {
    playerName
    team
    season
    minutesPlayed
    threeFg
    threeAttempts
    threePercent
    twoFg
    twoAttempts
    twoPercent
    ft
    fta
    ftPercent
    AST
    STL
    PTS
    fieldGoals
    fieldAttempts
    fieldPercent
    gamesStarted
  }
}
```
