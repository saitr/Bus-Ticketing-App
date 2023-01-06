from django.contrib import admin
from .models import Seat
# Register your models here.


class SeatInline(admin.TabularInline):
    model = Seat
    extra = 0

