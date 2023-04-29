from rest_framework import viewsets

from songs.models import Song, Artist
from songs.serializers import SongSerializer, ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
