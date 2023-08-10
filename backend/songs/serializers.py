from rest_framework import serializers
from .models import Artist, Line, Paragraph, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        exclude = ("paragraph",)


class ParagraphSerializer(serializers.ModelSerializer):
    lines = LineSerializer(read_only=True, many=True)

    class Meta:
        model = Paragraph
        exclude = ("song",)


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True, many=True)
    paragraphs = ParagraphSerializer(read_only=True, many=True)

    class Meta:
        model = Song
        fields = "__all__"

    def to_representation(self, instance):
        return super().to_representation(instance)
