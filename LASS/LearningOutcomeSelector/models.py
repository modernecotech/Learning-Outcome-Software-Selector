from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Learning Outcomes Software Selector model is structured on a semantic basis

class LearningOutcomes(models.Model):
    LearningOutcomeDescription_text= models.CharField(max_length=100)

    def __str__(self):
        return self.LearningOutcomeDescription_text

class LearningOutcomeSubject(models.Model):
    LearningOutcomeSubjectName_text = models.CharField(max_length=200)
    LinkedOutcome = models.ManyToManyField(
        LearningOutcomes
    )

    def __str__(self):
        return self.LearningOutcomeSubjectName_text

class Knowledge(models.Model):
    KnowledgeName_text=models.CharField(max_length=200)
    LinkedSubject = models.ManyToManyField(
        LearningOutcomeSubject
    )

    def __str__(self):
        return self.KnowledgeName_text

class Competences(models.Model):
    CompetenceName_text = models.CharField(max_length=200)
    LinkedKnowledge=models.ManyToManyField(
        Knowledge
    )
    def __str__(self):
        return self.CompetenceName_text

class Skills(models.Model):
    skillName_text=models.CharField(max_length=200)
    LinkedCompetence=models.ManyToManyField(
        Competences
    )

    def __str__(self):
        return self.skillName_text

class ApplicationFeatures(models.Model):
    FeatureName_text = models.CharField(max_length=200)
    LinkedSkills=models.ManyToManyField(
        Skills
    )

    def __str__(self):
        return self.FeatureName_text

class Application(models.Model):
    ApplicationName_text=models.CharField(max_length=200)
    Application_url=models.URLField()
    Application_logo_image=models.ImageField()
    ApplicationCostPerUserPerYear=models.PositiveIntegerField()
    LinkedApplicationFeatures=models.ManyToManyField(
        ApplicationFeatures
    )

    def __str__(self):
        return self.ApplicationName_text

class ExistingApplicationUsers(models.Model):
    ApplicationUser=models.CharField(max_length=200)
    ApplicationUser_url=models.URLField()
    LinkedApplication=models.ManyToManyField(
        Application
    )

    def __str__(self):
        return self.ApplicationUser

class ApplicationReviews(models.Model):
    ReviewPerson=models.CharField(max_length=200)
    ReviewText=models.TextField(max_length=1000)
    ReviewDate=models.DateTimeField(auto_now=True)
    ReviewRating=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)])
    ReviewedApplication=models.ForeignKey(Application,on_delete=models.CASCADE)

    def __str__(self):
        return self.ReviewPerson

