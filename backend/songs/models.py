from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100, blank=False)
    lyrics = models.JSONField(default=dict)
    artist = models.ManyToManyField("Artist", related_name="songs")
    picture_url = models.URLField(blank=True, null=True)

    translated_title = models.CharField(max_length=100, blank=True, null=True)
    translated_lyrics = models.JSONField(default=dict)
    # album = models.CharField(max_length=100)
    # release_date = models.DateField()
    # genre = models.CharField(max_length=100)
    # likes = models.IntegerField(default=0)
    # dislikes = models.IntegerField(default=0)


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    translated_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
