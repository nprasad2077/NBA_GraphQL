# GraphQL NBA Database Documentation

## Access the API

To interact with the NBA database, use the API endpoint provided below:

- **Endpoint URL**: [http://209.38.172.107/graphql/](http://209.38.172.107/graphql/)

This endpoint allows you to use the GraphiQL interface for testing and querying data.

## Usage Examples

### Query Player Totals for LeBron James

Retrieve comprehensive totals for LeBron James, including games played and team information:

```graphql
query {
  playerTotalsAll(name: "LeBron James") {
    playerName
    position
    season
    team
    games
    id
  }
}
```

### Query Players by Position and Sort by Total Rebounds

Fetch player data for the center position, sorted by total rebounds in descending order:

```graphql
query {
  playerTotalsAll(position: "C", ordering: "-total_rb") {
    age
    assists
    blocks
    defensiveRb
    effectFgPercent
    fieldAttempts
    fieldGoals
    ft
    fieldPercent
    ftAttempts
    ftPercent
    games
    gamesStarted
    id
    minutesPg
    offensiveRb
    personalFouls
    playerId
    playerName
    points
    position
    season
    steals
    team
    threeAttempts
    threeFg
    threePercent
    totalRb
    turnovers
    twoAttempts
    twoFg
    twoPercent
  }
}
```

### Query Advanced Stats for Houston Rockets Point Guards in 2019

Obtain advanced statistics for point guards from the Houston Rockets for the 2019 season, ordered by win shares:

```graphql
query {
  playerAdvancedAll(
    team: "HOU"
    season: 2019
    position: "PG"
    ordering: "-win_shares"
  ) {
    playerName
    position
    team
    season
    winShares
  }
}
```

### Query Detailed Advanced Stats for Kobe Bryant

Retrieve all available advanced statistical fields for Kobe Bryant:

```graphql
query {
  playerAdvancedAll(name: "Kobe Bryant") {
    id
    age
    assistPercent
    blockPercent
    box
    defensiveBox
    defensiveRbPercent
    defensiveWs
    ftr
    games
    minutesPlayed
    offensiveBox
    offensiveRbPercent
    offensiveWs
    per
    playerId
    playerName
    position
    stealPercent
    season
    team
    threePAr
    totalRbPercent
    tsPercent
    turnoverPercent
    usagePercent
    vorp
    winShares
    winSharesPer
  }
}
```

## API Features

### Endpoints

- **playerTotalsAll**: Retrieves aggregated player statistics.
- **playerAdvancedAll**: Provides advanced player statistics.

### Filters and Ordering

- **Filters Available**: Filter by `name`, `season`, `team`, `position`, `playerID`, or database `id (pk)`.
- **Ordering**: Use `-` before a category (e.g., `-points`) for descending order. Ascending order is the default.

### Data Fields

- **Player Totals Fields**: Access over 20 fields, including `playerName`, `season`, `games`, `points`, `rebounds`, and more.
- **Player Advanced Fields**: Includes advanced metrics such as `winShares`, `per`, `vorp`, and `usagePercent`.

For an exhaustive list of fields and detailed query examples, please consult the GraphQL schema documentation accessible through the [GraphiQL interface](http://209.38.172.107/graphql/).

This guide equips you with the necessary tools to explore and leverage the NBA_GraphQL API for your applications and research.
