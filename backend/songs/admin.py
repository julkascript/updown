from django.contrib import admin

from songs.models import Song, Artist

admin.site.register(Song)
admin.site.register(Artist)
