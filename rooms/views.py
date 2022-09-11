from django.shortcuts import render
from .models import Room
from rest_framework import viewsets, status
from .serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class RoomsViewset(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_room(request):
    room = RoomSerializer(data=request.data)
    if Room.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Duplicate data')
    if room.is_valid():
        room.save()
        return Response(room.data)
    else:
        return Response(status = status.HTTP_404_NOT_FOUND)