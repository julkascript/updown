from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100, blank=False)
    translated_title = models.CharField(max_length=100, blank=True, null=True)
    artist = models.ManyToManyField("Artist", related_name="songs")
    picture_url = models.URLField(blank=True, null=True)

    # lyrics = models.JSONField(default=dict)
    # translated_lyrics = models.JSONField(default=dict)
    # album = models.CharField(max_length=100)
    # release_date = models.DateField()
    # genre = models.CharField(max_length=100)
    # likes = models.IntegerField(default=0)
    # dislikes = models.IntegerField(default=0)


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    translated_name = models.CharField(max_length=100, blank=True, null=True)
    picture_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    name = models.CharField(max_length=100, blank=False)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="paragraphs")
    # order = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class Line(models.Model):
    paragraph = models.ManyToManyField(Paragraph, related_name="lines")
    content = models.TextField(blank=False)
    # translated_line = models.TextField(blank=True, null=True)
    # order = models.IntegerField(blank=False)

    def __str__(self):
        return self.content
