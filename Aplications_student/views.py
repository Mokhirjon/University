from django.shortcuts import render
from .models import AplicationModel
from .serializers import Aplicationserializer
from rest_framework import generics

# Create your views here.
class AplicationCreat(generics.CreateAPIView):
    queryset = AplicationModel.objects.all()
    serializer_class = Aplicationserializer

class Aplicationdelete(generics.DestroyAPIView):
    queryset = AplicationModel.objects.all()
    serializer_class = Aplicationserializer

class AplicationList(generics.ListCreateAPIView):
    queryset = AplicationModel.objects.all()
    serializer_class = Aplicationserializer

class details(generics.RetrieveAPIView):
    queryset = AplicationModel.objects.all()
    serializer_class = Aplicationserializer