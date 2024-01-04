from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(response):
    return HttpResponse("Welcome to little lemon web site!")
