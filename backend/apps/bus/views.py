from django.shortcuts import render
from .models import Bus
from .serializers import BusSerializer
from rest_framework import generics

# Create your views here.

class BusView(generics.ListCreateAPIView):
    # renderer_classes = [JSONRenderer]
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


