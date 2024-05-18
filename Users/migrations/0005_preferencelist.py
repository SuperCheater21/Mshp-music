# Generated by Django 5.0.4 on 2024-05-17 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genres', '0002_alter_genre_genre_name'),
        ('Users', '0004_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferenceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.ManyToManyField(blank=True, default=None, null=True, related_name='genres', to='Genres.genre')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.profile')),
            ],
        ),
    ]
