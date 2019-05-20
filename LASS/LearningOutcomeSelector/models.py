from django.db import models

# Learning Outcomes Software Selector model is structured on a semantic basis

class LearningOutcomes(models.Model):
    LearningOutcomeDescription_text= models.CharField(max_length=100)
    LearningCategories_field=models.ManyToManyField(
        LearningoutcomesList,
        through=''
    )

class LearningOutcomeList(models.Model):
    name_text = models.CharField(max_length=200)

class Application(models.Model):
    ApplicationName_text=models.CharField(max_length=200)
    Application_url=models.URLField()
    Application_logo_image=models.ImageField()

class ApplicationFeatures(models.Model):
    FeatureName_text = models.CharField(max_length=200)
    FeatureCategory=

class Skills(models.Model):
    skillName_text=models.Charfield(max_length=200)

class Competences(models.Model):
    CompetenceName_text = models.Charfield(max_length=200)

class Knowledge(models.Model):
    KnowledgeName_text=models.CharField(max_length=200)


