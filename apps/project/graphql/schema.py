import graphene

from apps.project.graphql.mutations import Mutation
from apps.project.graphql.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)

__all__=("schema",)
