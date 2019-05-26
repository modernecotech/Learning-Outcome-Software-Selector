from django.contrib import admin
from .models import LearningOutcomes, LearningOutcomeSubject, Knowledge, Competences, Skills, ApplicationFeatures, Application, ExistingApplicationUsers, ApplicationReviews

# Register your models here.

admin.site.register(LearningOutcomes)
admin.site.register(LearningOutcomeSubject)
admin.site.register(Knowledge)
admin.site.register(Competences)
admin.site.register(Skills)
admin.site.register(ApplicationFeatures)
admin.site.register(Application)
admin.site.register(ExistingApplicationUsers)
admin.site.register(ApplicationReviews)