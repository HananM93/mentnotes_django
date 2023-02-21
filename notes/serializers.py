# from rest_framework import serializers
# from .models import Note

# class NoteSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Note
#     fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'