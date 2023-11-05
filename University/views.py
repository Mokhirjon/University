from django.shortcuts import render
from rest_framework import generics
from .models import  UniversityModel
from .serializers import Universerializers

# Create your views here.
class UniverListAPiviews(generics.ListAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = Universerializers

class UniverCreate(generics.CreateAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = Universerializers

class UniverUpdate(generics.UpdateAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = Universerializers

class UniverDelete(generics.DestroyAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = Universerializers

class UniverDetails(generics.RetrieveAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = Universerializers