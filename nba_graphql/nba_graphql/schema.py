import graphene
import graphql_api.schema

class Query(graphql_api.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)