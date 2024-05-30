from openai import OpenAI
import os

from dotenv import load_dotenv
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from graphql_api.models import PlayerDataTotals, PlayerDataAdvanced

# Load environment variables from .env file
load_dotenv()

# Set OpenAI client and API key

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',               
)

class GenerateGraphQLQueryViewOllama(View):
    def post(self, request, *args, **kwargs):
        user_input = request.POST.get('user_input')
        print(f"User Input: {user_input}")  # Debug: Print user input
        
        # Fetch some relevant data from your models to provide context to GPT-3
        example_stats = PlayerDataTotals.objects.filter(team='HOU', season=2019)[:5]
        example_stats_adv = PlayerDataAdvanced.objects.filter(team='LAL', season=2006)[:5]
        #print(f"Fetched {len(example_stats)} example stats")  # Debug: Print number of fetched stats
        
        example_data = ""

        '''
        for stat in example_stats:
            example_data += f"- Player: {stat.playerName}, Points: {stat.points}, Assists: {stat.assists}, Games: {stat.games}, Position: {stat.position}\n"
        '''
        # print(f"Example Data: {example_data}")  # Debug: Print example data
        
        # Define the GraphQL schema for the AI assistant
        graphql_schema = """
        type Query {
            playerTotals(team: String, season: Int, ordering: String, limit: Int, name: String, id: Int, playerId: String): [PlayerTotals]
            playerTotalsPlayoffs(team: String, season: Int, ordering: String, limit: Int, name: String, id: Int, playerId: String): [PlayerTotalsPlayoffs]
            playerAdvanced(team: String, season: Int, ordering: String, limit: Int, name: String, id: Int, playerId: String): [PlayerAdvanced]
            playerAdvancedPlayoffs(team: String, season: Int, ordering: String, limit: Int, name: String, id: Int, playerId: String): [PlayerAdvancedPlayoffs]
        }

        type playerTotals {
            playerName: String
            points: Int
            assists: Int
            games: Int
            position: String
            team: String
            season: Int
            playerId: String
            id: Int
            totalRb: Int: Int
            offensiveRb: Int
            defensiveRb: Int
            blocks: Int
            steals: Int
            turnovers: Int
            ft: Int
            ftAttempts: Decimal
            ftPercent: Decimal
            twoAttempts: Int
            twoFg: Int
            twoPercent: Decimal
            threeAttempts: Int
            threeFg: Int
            threePercent: Decimal
            effectFgPercent: Decimal
            fieldAttempts: Int
            fieldGoals: Int
            fieldPercent: Decimal
            personalFouls: Int
            minutesPg: Int
            gamesStarted: Int
        }

        type playerAdvanced {
            id: Int
            playerId: String
            playerName: String
            position: String
            team: String
            season: Int
            games: Int
            minutesPlayed: Int
            winShares: Decimal
            offensiveWs: Decimal
            defensiveWs: Decimal
            winSharesPer: Decimal
            box: Decimal
            offensiveBox: Decimal
            defensiveBox: Decimal
            per: Decimal
            vorp: Decimal
            usagePercent: Decimal
            tsPercent: Decimal
            ftr: Decimal
            assistPercent: Decimal
            blockPercent: Decimal
            totalRbPercent: Decimal
            offensiveRbPercent: Decimal
            defensiveRbPercent: Decimal
            stealPercent: Decimal
            threePAr: Decimal
            turnoverPercent: Decimal
            age: Int
        }
        
        type playerTotalsPlayoffs {
            playerName: String
            points: Int
            assists: Int
            games: Int
            position: String
            team: String
            season: Int
            playerId: String
            id: Int
            totalRb: Int: Int
            offensiveRb: Int
            defensiveRb: Int
            blocks: Int
            steals: Int
            turnovers: Int
            ft: Int
            ftAttempts: Decimal
            ftPercent: Decimal
            twoAttempts: Int
            twoFg: Int
            twoPercent: Decimal
            threeAttempts: Int
            threeFg: Int
            threePercent: Decimal
            effectFgPercent: Decimal
            fieldAttempts: Int
            fieldGoals: Int
            fieldPercent: Decimal
            personalFouls: Int
            minutesPg: Int
            gamesStarted: Int
        }
        
        type playerAdvancedPlayoffs {
            id: Int
            playerId: String
            playerName: String
            position: String
            team: String
            season: Int
            games: Int
            minutesPlayed: Int
            winShares: Decimal
            offensiveWs: Decimal
            defensiveWs: Decimal
            winSharesPer: Decimal
            box: Decimal
            offensiveBox: Decimal
            defensiveBox: Decimal
            per: Decimal
            vorp: Decimal
            usagePercent: Decimal
            tsPercent: Decimal
            ftr: Decimal
            assistPercent: Decimal
            blockPercent: Decimal
            totalRbPercent: Decimal
            offensiveRbPercent: Decimal
            defensiveRbPercent: Decimal
            stealPercent: Decimal
            threePAr: Decimal
            turnoverPercent: Decimal
            age: Int
        }
    
        """

        # Construct the prompt with additional context
        prompt = f"""
        User input: "{user_input}"
        Given the following player stats data:
        {example_stats}
        {example_stats_adv}

        GraphQL Schema:
        {graphql_schema}

        Please generate a valid GraphQL query based on the user input. Ensure the 'ordering' variable is a single word with a '-' sign in front, indicating the field to order by in descending order. The ordering string must be in snake case even though the GraphQL query is in camel case.
        Always use NBA team abbreviations for the 'team' field. Convert all user input to NBA team names in query.
        If a field is not provided do not include it. Always return all fields unless specified otherwise in the user input.
        ONLY return the query. Do not add any notes or comments.

        Example:
        query {{
          playerTotals(team: "LAL", season: 2000, ordering: "-points", limit: 20) {{
            playerName
            points
            assists
            games
            position
            team
            season
            playerId
            id
            totalRb
            offensiveRb
            defensiveRb
            blocks
            steals
            turnovers
            ft
            ftAttempts
            ftPercent
            twoAttempts
            twoFg
            twoPercent
            threeAttempts
            threeFg
            threePercent
            effectFgPercent
            fieldAttempts
            fieldGoals
            fieldPercent
            personalFouls
            minutesPg
            gamesStarted
          }}
        }}
        
        GraphQL query:
        """
        #print(f"Prompt: {prompt}")  # Debug: Print the prompt
        
        try:
            response = client.chat.completions.create(
                model="llama3",  # Updated to use the 'llama3' model
                messages=[
                    {"role": "system", "content": "You are an assistant that helps generate GraphQL queries."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=3500,
                n=1, 
                temperature=0.7
            )
           # print(f"OpenAI Response: {response}")  # Debug: Print the raw response
            
            graphql_query = response.choices[0].message.content.strip()
            
            graphql_query = graphql_query.replace('```graphql', '').replace('```', '').strip()
            print(f"Generated GraphQL Query: {graphql_query}")  # Debug: Print the generated GraphQL query
            
            return JsonResponse({'graphql_query': graphql_query}, status=200)
        
        except Exception as e:
            print(f"Error: {e}")  # Debug: Print the error
            return JsonResponse({'error': str(e)}, status=500)
