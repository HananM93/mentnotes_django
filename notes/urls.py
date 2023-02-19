from django.urls import path
from .views import Notes,NotesDetail  #home

urlpatterns = [
    # path('home', home, name='home'),
    path('', Notes.as_view(), name='notes'),
    path('<int:pk>', NotesDetail.as_view(), name='notes_details')
]
