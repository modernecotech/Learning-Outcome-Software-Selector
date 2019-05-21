from django.shortcuts import render
from django.http import HttpResponse

#stuff for the REST framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Learning Outcomes Software Selector")

