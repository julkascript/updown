from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100, blank=False)
    lyrics = models.JSONField(default=dict)
    artist = models.ManyToManyField("Artist", related_name="songs")
    picture_url = models.URLField(blank=True, null=True)
    # album = models.CharField(max_length=100)
    # release_date = models.DateField()
    # genre = models.CharField(max_length=100)
    # likes = models.IntegerField(default=0)
    # dislikes = models.IntegerField(default=0)


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
