from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Test View for Homepage


def home(request):
  return HttpResponse('<h1> MY HOME PAGE </h1>')


# Create your views here.

class Notes(APIView):
    def get(self,request):
        note = Note.objects.all()
        