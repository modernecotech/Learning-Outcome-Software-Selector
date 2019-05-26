import graphene

from graphene_django.types import DjangoObjectType

from .models import LearningOutcomes, LearningOutcomeSubject, Knowledge, Competences, Skills, ApplicationFeatures, Application, ExistingApplicationUsers, ApplicationReviews

class LearningOutcomesType(DjangoObjectType):
    class Meta:
        model= LearningOutcomes


class LearningOutcomeSubjectType(DjangoObjectType):
    class Meta:
        model= LearningOutcomeSubject


class KnowledgeType(DjangoObjectType):
    class Meta:
        model= Knowledge


class Query(object):
    all_learningoutcomes=graphene.List(LearningOutcomesType)
    all_learningoutcomesubjects=graphene.List(LearningOutcomeSubjectType)
    