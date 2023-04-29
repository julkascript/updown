from rest_framework import serializers
from .models import Artist, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True, many=True)

    class Meta:
        model = Song
        fields = ("artist", "title", "lyrics", "id")

    def to_representation(self, instance):
        return super().to_representation(instance)
