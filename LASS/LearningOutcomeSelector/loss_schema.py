from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import LearningOutcomes, LearningOutcomeSubject, Knowledge, Competences, Skills, ApplicationFeatures, Application, ExistingApplicationUsers, ApplicationReviews

class LearningOutcomesType(DjangoObjectType):
    class Meta:
        model= LearningOutcomes
        filter_fields={
            'LearningOutcomeDescription_text':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class LearningOutcomeSubjectType(DjangoObjectType):
    class Meta:
        model = LearningOutcomeSubject
        filter_fields={
            'LearningOutcomeSubjectName_text':['exact', 'icontains', 'istartswith'],
            'LinkedOutcome':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class KnowledgeType(DjangoObjectType):
    class Meta:
        model= Knowledge
        filter_fields={
            'KnowledgeName_text':['exact', 'icontains', 'istartswith'],
            'LinkedSubject':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class CompetencesType(DjangoObjectType):
    class Meta:
        model= Competences
        filter_fields={
            'CompetenceName_text':['exact', 'icontains', 'istartswith'],
            'LinkedKnowledge':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class SkillsType(DjangoObjectType):
    class Meta:
        model= Skills
        filter_fields={
            'skillName_text':['exact', 'icontains', 'istartswith'],
            'LinkedCompetence':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class ApplicationFeaturesType(DjangoObjectType):
    class Meta:
        model= ApplicationFeatures
        filter_fields={
            'FeatureName_text':['exact', 'icontains', 'istartswith'],
            'LinkedSkills':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class ApplicationType(DjangoObjectType):
    class Meta:
        model= Application
        filter_fields={
            'ApplicationName_text':['exact', 'icontains', 'istartswith'],
            'Application_url':['exact', 'icontains', 'istartswith'],
            'ApplicationCostPerUserPerYear':['exact', 'icontains', 'istartswith'],
            'LinkedApplicationFeatures':['exact', 'icontains', 'istartswith'],

        }
        interfaces = (relay.Node, )

class ExistingApplicationUsersType(DjangoObjectType):
    class Meta:
        model= ExistingApplicationUsers
        filter_fields={
            'ApplicationUser':['exact', 'icontains', 'istartswith'],
            'ApplicationUser_url':['exact', 'icontains', 'istartswith'],
            'LinkedApplication':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class ApplicationReviewsType(DjangoObjectType):
    class Meta:
        model= ApplicationReviews
        filter_fields={
            'ReviewPerson':['exact', 'icontains', 'istartswith'],
            'ReviewText':['exact', 'icontains', 'istartswith'],
            'ReviewDate':['exact', 'icontains', 'istartswith'],
            'ReviewRating':['exact', 'icontains', 'istartswith'],
#            'ReviewedApplication':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    all_learningoutcomes=DjangoFilterConnectionField(LearningOutcomesType)
    all_LearningOutcomeSubjects=DjangoFilterConnectionField(LearningOutcomeSubjectType)
    all_Knowledge = DjangoFilterConnectionField(KnowledgeType)
    all_Competences = DjangoFilterConnectionField(CompetencesType)
    all_Skills = DjangoFilterConnectionField(SkillsType)    
    all_ApplicationFeatures = DjangoFilterConnectionField(ApplicationFeaturesType)    
    all_Application = DjangoFilterConnectionField(ApplicationType)
    all_ExistingApplicationUsers = DjangoFilterConnectionField(ExistingApplicationUsersType)
    all_ApplicationReviews = DjangoFilterConnectionField(ApplicationReviewsType)

    learningoutcomes=relay.Node.Field(LearningOutcomesType)
    learningoutcomesubject=relay.Node.Field(LearningOutcomeSubjectType)
    knowledge=relay.Node.Field(KnowledgeType)
    competences=relay.Node.Field(CompetencesType)
    skills=relay.Node.Field(SkillsType)
    applicationfeatures=relay.Node.Field(ApplicationFeaturesType)
    application=relay.Node.Field(ApplicationType)
    applicationusers=relay.Node.Field(ExistingApplicationUsersType)
    applicationreviews=relay.Node.Field(ApplicationReviewsType)

'''
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
'''