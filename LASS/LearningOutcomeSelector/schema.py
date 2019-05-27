import graphene
import LearningOutcomeSelector.loss_schema

class Query(LearningOutcomeSelector.loss_schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
