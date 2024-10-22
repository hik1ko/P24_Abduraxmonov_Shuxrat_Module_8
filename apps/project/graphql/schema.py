import graphene

from apps.project.graphql.query import Query

schema = graphene.Schema(query=Query)

__all__=("schema",)
