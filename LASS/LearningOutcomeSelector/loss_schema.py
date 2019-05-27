import graphene

from graphene_django.types import DjangoObjectType

from .models import LearningOutcomes, LearningOutcomeSubject, Knowledge, Competences, Skills, ApplicationFeatures, Application, ExistingApplicationUsers, ApplicationReviews

class LearningOutcomesType(DjangoObjectType):
    class Meta:
        model= LearningOutcomes


class LearningOutcomeSubjectType(DjangoObjectType):
    class Meta:
        model = LearningOutcomeSubject


class KnowledgeType(DjangoObjectType):
    class Meta:
        model= Knowledge


class CompetencesType(DjangoObjectType):
    class Meta:
        model= Competences


class SkillsType(DjangoObjectType):
    class Meta:
        model= Skills


class ApplicationFeaturesType(DjangoObjectType):
    class Meta:
        model= ApplicationFeatures


class ApplicationType(DjangoObjectType):
    class Meta:
        model= Application


class ExistingApplicationUsersType(DjangoObjectType):
    class Meta:
        model= ExistingApplicationUsers


class ApplicationReviewsType(DjangoObjectType):
    class Meta:
        model= ApplicationReviews



class Query(object):
    all_learningoutcomes=graphene.List(LearningOutcomesType)
    all_learningoutcomesubjects=graphene.List(LearningOutcomeSubjectType)
    all_knowledge = graphene.List(KnowledgeType)
    all_Competences = graphene.List(CompetencesType)
    all_Skills = graphene.List(SkillsType)    
    all_ApplicationFeatures = graphene.List(ApplicationFeaturesType)    
    all_Application = graphene.List(ApplicationType)
    all_ExistingApplicationUsers = graphene.List(ExistingApplicationUsersType)
    all_ApplicationReviews = graphene.List(ApplicationReviewsType)

    def resolve_all_learningoutcomes(self,info,**kwargs):
        return LearningOutcomes.objects.all()
    
    def resolve_all_learningoutcomessubjects(self,info,**kwargs):
        return LearningOutcomeSubject.objects.all()
        
    def resolve_all_knowledge(self,info,**kwargs):
        return Knowledge.objects.all()
        
    def resolve_all_Competences(self,info,**kwargs):
        return Competences.objects.all()

    def resolve_all_Skills(self,info,**kwargs):
        return Skills.objects.all()

    def resolve_all_ApplicationFeatures(self,info,**kwargs):
        return ApplicationFeatures.objects.all()

    def resolve_all_Application(self,info,**kwargs):
        return Application.objects.all()

    def resolve_all_ExistingApplicationUsers(self,info,**kwargs):
        return ExistingApplicationUsers.objects.all()
    
    def resolve_all_ApplicationReviews(self,info,**kwargs):
        return ApplicationReviews.objects.all()
