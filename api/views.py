from django.shortcuts import render
from rest_framework import viewsets

from .serializers import KitchenSerializer, LivingRoomSerializer
from realestate.models import KitchenRoom, LivingRoom
# Create your views here.


class KitchenViewSet(viewsets.ModelViewSet):
    queryset = KitchenRoom.objects.all()
    serializer_class = KitchenSerializer


class LivingRoomViewSet(viewsets.ModelViewSet):
    queryset = LivingRoom.objects.all()
    serializer_class = LivingRoomSerializer
