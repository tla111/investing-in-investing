from django.shortcuts import render
from rest_framework import viewsets

from .serializers import KitchenSerializer, LivingRoomSerializer, BedRoomSerializer
from realestate.models import KitchenRoom, LivingRoom, BedRoom
# Create your views here.


class KitchenViewSet(viewsets.ModelViewSet):
    queryset = KitchenRoom.objects.all()
    serializer_class = KitchenSerializer


class LivingRoomViewSet(viewsets.ModelViewSet):
    queryset = LivingRoom.objects.all()
    serializer_class = LivingRoomSerializer


class BedRoomViewSet(viewsets.ModelViewSet):
    queryset = BedRoom.objects.all()
    serializer_class = BedRoomSerializer
