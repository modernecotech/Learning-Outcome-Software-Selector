from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import LearningOutcomes, LearningOutcomeSubject, Knowledge, Competences, Skills, ApplicationFeatures, Application, ExistingApplicationUsers, ApplicationReviews
from .forms import LearningQueryForm

#stuff for the REST framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    # if this is a POST request we need to process the form data
    if request.method=='POST':
        # create a form instance and populate it with data from the request:
        form=LearningQueryForm(request.POST)
        if form.is_valid():
            #process data form

            #then redirect to a new url
            return HttpResponseRedirect('/result')
    else:
        form = LearningQueryForm()
        
    return render(request,'LearningQuestion.html', {'form':form})
