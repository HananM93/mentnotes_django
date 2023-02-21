from django.urls import path
from .views import NotesList, NotesPost, NotesDetail

urlpatterns = [
    path('', NotesList.as_view(), name='notes'),
    path('note/', NotesPost.as_view(), name='notes_post'),
    path('<int:pk>', NotesDetail.as_view(), name='notes_details')
]
