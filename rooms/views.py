from django.shortcuts import render
from .models import Room
from rest_framework import viewsets
from .serializers import RoomSerializer

class RoomsViewset(viewsets.ModelViewSet):
    serializer = RoomSerializer
    queryset = Room.objects.all()