from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Note
from .serializers import NoteSerializer


# Test View for Homepage


# def home(request):
#   return HttpResponse('<h1> MY HOME PAGE </h1>')


# Create your views here.



class Notes(APIView):

  
    # Get all notes
  
    def get(self,request):
        notes = Note.objects.all()
        data = NoteSerializer(notes, many=True).data
        return Response(data)
        
    # Create a new note
  
    def post(self,request):
      data = request.data
      if note.is_valid():
        note.save()
        return Response(note.data, status=status.HTTP_201_CREATED)
      else:
        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)

  

class NotesDetail(APIView):

  #  Get a note

  def get(self, request, pk):
    note = get_object_or_404(Note, pk=pk)
    data = NoteSerializer(note).data
    return Response(data)

#  Update a note

  def put (self,request, pk):
    data=request.data
    note= get_object_or_404(Note,pk=pk)
    updated = NoteSerializer(note, data=request.data, partial=True)
    if updated.is_valid():
      updated.save()
      return Response(updated.data)
    else:
      return Response(updated.error, status=status.HTTP_400_BAD_REQUEST)

      #  Delete a note

  def delete(self,request,pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return Response(status=status.HTTP_400_BAD_REQUEST)