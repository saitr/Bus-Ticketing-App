from django.contrib import admin
from apps.seat.admin import SeatInline
from .models import Bus
# Register your models here.
from apps.seat.models import Seat

# admin.site.register(Bus)
# admin.site.register(Seat)

# class SeatInline(admin.TabularInline):
#     model = Seat
#     extra = 0


class BusAdmin(admin.ModelAdmin):
    inlines = [SeatInline]
    class Meta:
        model = Bus



admin.site.register(Bus,BusAdmin)
# admin.site.register(SeatInline)
