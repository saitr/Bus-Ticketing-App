from rest_framework import serializers
from .models import Bus
from apps.seat.models import Seat
from apps.seat.serializers import SeatSerializer

class SeatBusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Seat
        fields = '__all__'



class BusSerializer(serializers.ModelSerializer):
    seats = SeatBusSerializer(many=True,source='seat_details')
    
    class Meta():
        model = Bus
        fields = ['bus_name','bus_number','route','arrival_time','departure_time','image','seats']


