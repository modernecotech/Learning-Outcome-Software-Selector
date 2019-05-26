import graphene
import loss_schema

class Query(loss_schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
