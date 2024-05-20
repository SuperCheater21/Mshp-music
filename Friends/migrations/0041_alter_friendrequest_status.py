# Generated by Django 5.0.4 on 2024-05-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friends', '0040_alter_friendrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('accepted', 'accepted'), ('send', 'send')], default='send', max_length=8),
        ),
    ]