from django.db import models
from cloudinary.models import CloudinaryField
# from apps.seat.models import Seat
# Create your models here.

class Bus(models.Model):
    class Meta(object):
        db_table = 'Bus'
        verbose_name = 'Bus'
    
    bus_name = models.CharField('Bus Name',max_length=20,blank = False,null=False,default= None)
    bus_number = models.CharField('Bus Number',max_length=10,blank = False,null=False,default= None)
    route = models.CharField('Route',max_length=50,blank = False,null=False)
    arrival_time = models.DateTimeField('Arrival Timing')
    departure_time = models.DateTimeField('Departure Timing')
    # seats = models.ForeignKey(Seat,null=False,blank = False,on_delete=models.CASCADE)
    # seat = models.ForeignKey(Seat,null=False,blank = False,on_delete=models.CASCADE)
    
    image = CloudinaryField('Image',blank=False)    

    @property
    def seat_details(self):
        return self.related_bus.all()