from django.urls import path
from . import views

urlpatterns = [
    path('',views.BusView.as_view(),name='bus_view')
]