# Generated by Django 5.0.4 on 2024-05-16 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genres', '0001_initial'),
        ('Playlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='genre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Genres.genre'),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]