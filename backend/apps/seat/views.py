from django.shortcuts import render
from .models import Seat
from .serializers import SeatSerializer
from rest_framework import generics
# Create your views here.

class SeatView(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
