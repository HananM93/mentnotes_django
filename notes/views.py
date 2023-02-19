from django.shortcuts import render
from django.http import HttpResponse




# Test View for Homepage


def home(request):
  return HttpResponse('<h1> MY HOME PAGE </h1>')


# Create your views here.
