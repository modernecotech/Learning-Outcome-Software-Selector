from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Learning Outcomes Software Selector model is structured on a semantic basis

class LearningOutcomes(models.Model):
    LearningOutcomeDescription_text= models.CharField(max_length=100)

class LearningOutcomeSubject(models.Model):
    LearningOutcomeSubjectName_text = models.CharField(max_length=200)
    LinkedOutcome = models.ManyToManyField(
        LearningOutcomes
    )

class Knowledge(models.Model):
    KnowledgeName_text=models.CharField(max_length=200)
    LinkedSubject = models.ManyToManyField(
        LearningOutcomeSubject
    )

class Competences(models.Model):
    CompetenceName_text = models.CharField(max_length=200)
    LinkedKnowledge=models.ManyToManyField(
        Knowledge
    )

class Skills(models.Model):
    skillName_text=models.CharField(max_length=200)
    LinkedCompetence=models.ManyToManyField(
        Competences
    )

class ApplicationFeatures(models.Model):
    FeatureName_text = models.CharField(max_length=200)
    LinkedSkills=models.ManyToManyField(
        Skills
    )

class Application(models.Model):
    ApplicationName_text=models.CharField(max_length=200)
    Application_url=models.URLField()
    Application_logo_image=models.ImageField()
    ApplicationCostPerUserPerYear=models.PositiveIntegerField()
    LinkedApplicationFeatures=models.ManyToManyField(
        ApplicationFeatures
    )

class ExistingApplicationUsers(models.Model):
    ApplicationUser=models.CharField(max_length=200)
    ApplicationUser_url=models.URLField()
    LinkedApplication=models.ManyToManyField(
        Application
    )

class ApplicationReviews(models.Model):
    ReviewPerson=models.CharField(max_length=200)
    ReviewText=models.TextField(max_length=1000)
    ReviewDate=models.DateTimeField(auto_now=True)
    ReviewRating=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)])
    ReviewedApplication=models.ForeignKey(Application,on_delete=models.CASCADE)

