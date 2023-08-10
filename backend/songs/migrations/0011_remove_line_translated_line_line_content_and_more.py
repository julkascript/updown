# Generated by Django 4.1.7 on 2023-08-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0010_remove_song_lyrics_song_translated_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='translated_line',
        ),
        migrations.AddField(
            model_name='line',
            name='content',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paragraph',
            name='name',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]