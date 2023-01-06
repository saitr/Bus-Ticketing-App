from django.urls import path

from . import views

urlpatterns = [
    path('',views.SeatView.as_view(),name = 'seatview')
]