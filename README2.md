## Installation Instructions

To get started with the NBA_GraphQL API, follow these steps to set up your environment. This guide assumes you have Python and pip installed on your system.

1. **Clone the Repository**
   First, clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/NBA_GraphQL.git
   cd NBA_GraphQL
   ```

2. **Set Up a Virtual Environment**
   It's recommended to use a virtual environment for Python projects. This keeps your dependencies for the project separate and organized. Create and activate a virtual environment with:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows, activation is slightly different:

   ```bash
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required Python packages for the API:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Server**
   Once the dependencies are installed, you can start the GraphQL server with:

   ```bash
   python manage.py runserver
   ```

   This command will start the Django development server, making the GraphQL endpoint accessible at [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/).

## Usage Examples

### Querying Player Totals

To query player totals for LeBron James, you can use the following GraphQL query:

```graphQL
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

### Querying Players by Position and Ordering

To query players by position and order them by total rebounds in descending order (returns all fields:

```graphQL
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

### Advanced Player Stats

To query advanced stats for players from the Houston Rockets in the 2019 season, playing as Point Guards, ordered by win shares:

```graphQL
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

### Querying a Specific Player's Advanced Stats

For detailed advanced stats for Kobe Bryant (returns all fields):

```graphQL
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

## API Endpoints and GraphQL Queries

The NBA_GraphQL API provides a rich set of endpoints to query player statistics, both total and advanced, along with the ability to filter and order results based on various criteria such as player name, team, season, and position.

### Endpoints

- **playerTotalsAll**: Fetches aggregated player statistics.
- **playerAdvancedAll**: Fetches advanced player statistics.

### Filters and Ordering

- **Filters**: `name`, `season`, `team`, `position`, `playerID`, `id (pk)`.
- **Ordering Functions**: Support for ascending and descending order based on statistical categories.

### Fields Available for Retrieval

- **Player Totals**: Includes fields such as `playerName`, `team`, `season`, `games`, `points`, `assists`, `rebounds`, `age`, `blocks`, `defensiveRB`, `effectFGPercent`, etc.
- **Player Advanced**: Includes fields such as `playerName`, `team`, `season`, `winShares`, `per`, `vorp`, `usagePercent`, etc.

For a comprehensive list of fields and detailed examples of queries and mutations, please refer to the GraphQL schema documentation available at the GraphiQL interface.

By following these instructions and examples, you should be well-equipped to start exploring and utilizing the NBA_GraphQL API for your projects.
