from django.contrib import admin

from songs.models import Line, Paragraph, Song, Artist

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Paragraph)
admin.site.register(Line)


