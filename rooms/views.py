from django.shortcuts import render
from .models import Room
from rest_framework import viewsets
from .serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class RoomsViewset(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

@api_view(['GET', 'POST'])
def create_room(request):
    if request.method == 'POST':
        return Response({"message": "data posted"})
    return Response({"message": "data get"})