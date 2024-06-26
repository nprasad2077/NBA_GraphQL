# GraphQL NBA Database

## Query the deployed API endpoint

[Guide on how to use this API.](https://github.com/nprasad2077/NBA_GraphQL/wiki)

[https://nbaapi.com/graphql/](https://nbaapi.com/graphql/)

## Usage Examples

### Querying Player Totals

To query player totals for LeBron James, you can use the following GraphQL query:

```graphQL
query {
  playerTotals(name: "LeBron James") {
    playerName
    position
    season
    team
    games
    id
  }
}
```

This will return the player name, position, season, team, games played, and database id for every row entry in the database matching name for 'LeBron James'.

### Querying Players by Position and Ordering

To query players by position and order them by total rebounds in descending order (returns all possible fields):

```graphQL
query {
  playerTotals(position: "C", ordering: "-total_rb") {
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
  playerAdvanced(
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
  playerAdvanced(name: "Kobe Bryant") {
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

- **playerTotals**: Fetches aggregated player statistics.
- **playerAdvanced**: Fetches advanced player statistics.

### Filters and Ordering

- **Filters**: `name`, `season`, `team`, `position`, `playerID`, `id (pk)`.
- **Ordering Functions**: Support for ascending and descending order based on statistical categories. Put a '-' sign in front of categories to obtain descending order. For example `-points` in the ordering query paramater would return results by points in descending order.

### Fields Available for Retrieval

- **Player Totals**: Includes fields such as `playerName`, `team`, `season`, `games`, `points`, `assists`, `rebounds`, `age`, `blocks`, `defensiveRB`, `effectFGPercent`, `fieldAttempts`, `fieldGoals`, `ft`, `fieldPercent`, `ftAttempts`, `ftPercent`, `gamesStarted`, `id (pkey)`, `minutesPG`, etc.
- **Player Advanced**: Includes fields such as `playerName`, `team`, `season`, `winShares`, `per`, `vorp`, `usagePercent`, etc.

For a comprehensive list of fields and detailed examples of queries and mutations, please refer to the GraphQL schema documentation available at the [GraphiQL interface.](http://209.38.172.107/graphql/)

By following these instructions and examples, you should be well-equipped to start exploring and utilizing the NBA_GraphQL API for your projects.

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

## Here's a trippy take on the GraphQL and NBA blend: a player, amidst a swirl of colors, dribbles a ball that's a universe in itself, echoing the patterns of GraphQL in a cosmic court. 🌀🏀🌌

![DALL·E 2023-11-14 00.27.45 - A vibrant, psychedelic image blending the GraphQL logo with the NBA logo, showing a basketball player dribbling a ball designed with the GraphQL patte](./images/DALL·E2.png)

## In this cosmic fusion, the GraphQL logo intertwines with the NBA's spirit, creating a surreal basketball extravaganza. Imagine this ball spinning in an otherworldly court, where the game transcends reality. 🌌🏀✨

![DALL·E 2023-11-14 00.27.03 - A surreal image combining the GraphQL logo and the NBA logo, featuring a colorful basketball with the GraphQL logo pattern, spinning in a cosmic baske](./images/DALL·E1.png)

## More images :D

"Clip art to represent the NBA GraphQL data point and database that I will be assembling"

![GraphQLxNBA](images/export1.png)

![retroNBAData](images/export2.png)

![Behold the cosmic fusion of sports and data! A basketball transforming into a vibrant database, a digital dream of NBA stats. 🌌🏀💾](images/DALL·E3.png)
