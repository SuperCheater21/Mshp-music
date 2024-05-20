# Generated by Django 5.0.4 on 2024-05-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genres', '0002_alter_genre_genre_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='genre_name',
        ),
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]