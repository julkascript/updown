from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100, blank=False)
    artist = models.CharField(max_length=100, blank=False)
    lyrics = models.JSONField(default=dict)
    # album = models.CharField(max_length=100)
    # release_date = models.DateField()
    # genre = models.CharField(max_length=100)
    # likes = models.IntegerField(default=0)
    # dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " - " + self.artist
