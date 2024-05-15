from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPEN_AI_KEY'))

from dotenv import load_dotenv
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from graphql_api.models import PlayerDataTotals

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key

class GenerateGraphQLQueryView(View):
    def post(self, request, *args, **kwargs):
        user_input = request.POST.get('user_input')
        print(f"User Input: {user_input}")  # Debug: Print user input
        
        # Fetch some relevant data from your models to provide context to GPT-3
        example_stats = PlayerDataTotals.objects.filter(team='HOU', season=2019)[:5]
        print(f"Fetched {len(example_stats)} example stats")  # Debug: Print number of fetched stats
        
        example_data = ""
        for stat in example_stats:
            example_data += f"- Player: {stat.player_name}, Points: {stat.points}, Assists: {stat.assists}, Games: {stat.games}, Position: {stat.position}\n"
        print(f"Example Data: {example_data}")  # Debug: Print example data
        
        # Define the GraphQL schema for the AI assistant
        graphql_schema = """
        type Query {
            playerDataTotals(team: String, season: Int, ordering: String, limit: Int, name: String, id: Int, playerId: String): [PlayerDataTotals]
        }

        type PlayerDataTotals {
            player_name: String
            points: Int
            assists: Int
            games: Int
            position: String
            team: String
            season: Int
            playerId: String
            id: Int
        }
        """

        # Construct the prompt with additional context
        prompt = f"""
        User input: "{user_input}"
        Given the following player stats data:
        {example_data}

        GraphQL Schema:
        {graphql_schema}

        Please generate a valid GraphQL query based on the user input. Ensure the 'ordering' variable is a single word with a '-' sign in front, indicating the field to order by in descending order.
        If a field is not provided do not include it.

        Example:
        query {{
          playerDataTotals(team: "LAL", season: 2000, ordering: "-points", limit: 20) {{
            player_name
            points
            assists
            games
            position
            team
            season
            playerId
            id
          }}
        }}
        
        GraphQL query:
        """
        print(f"Prompt: {prompt}")  # Debug: Print the prompt
        
        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo",  # Updated to use the 'gpt-4' model
                messages=[
                    {"role": "system", "content": "You are an assistant that helps generate GraphQL queries."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2500,
                n=1,
                stop=["\n\n"],  # You can specify stop sequences to prevent the model from going off-topic
                temperature=0.7
            )
            print(f"OpenAI Response: {response}")  # Debug: Print the raw response
            
            graphql_query = response.choices[0].message.content.strip()
            print(f"Generated GraphQL Query: {graphql_query}")  # Debug: Print the generated GraphQL query
            
            return JsonResponse({'graphql_query': graphql_query}, status=200)
        
        except Exception as e:
            print(f"Error: {e}")  # Debug: Print the error
            return JsonResponse({'error': str(e)}, status=500)
