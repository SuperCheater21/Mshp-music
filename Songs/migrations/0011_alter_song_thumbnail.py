# Generated by Django 5.0.4 on 2024-05-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0010_alter_song_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='thumbnail',
            field=models.ImageField(default='audio_file/images/thumbnail.png', help_text='.jpg, .png, .jpeg, .gif, .svg supported', upload_to='audio_files/images'),
        ),
    ]