from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from musiclibrary.models import Song
from rest_framework import status

# Create your views here.


@api_view(["GET", "POST"])
def music_list(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = MusicSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def music_detail(request, pk):
    song=get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer=MusicSerializer(song);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)