# Generated by Django 4.2.11 on 2024-05-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0002_alter_song_artist_alter_song_audio_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to=''),
        ),
    ]