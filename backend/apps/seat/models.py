from django.db import models
from apps.bus.models import Bus
# Create your models here.



class Seat(models.Model):
    class Meta(object):
        db_table = 'seat'
        verbose_name = ('seat')
    bus = models.ForeignKey(Bus, related_name= 'related_bus',blank=True, null=True,on_delete=models.SET_NULL)
    seat_name = models.CharField('Seat',max_length=5,blank=False,null=False,default=None)
    seat_number = models.CharField('Seat Number',max_length=5,null=False,blank=False,default=None)