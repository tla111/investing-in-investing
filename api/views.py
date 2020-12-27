from django.shortcuts import render
from rest_framework import viewsets

from .serializers import KitchenSerializer
from realestate.models import KitchenRoom
# Create your views here.


class KitchenViewSet(viewsets.ModelViewSet):
    queryset = KitchenRoom.objects.all()
    serializer_class = KitchenSerializer