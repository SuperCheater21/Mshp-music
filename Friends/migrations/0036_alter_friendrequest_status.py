# Generated by Django 5.0.4 on 2024-05-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friends', '0035_alter_friendrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('send', 'send'), ('rejected', 'rejected')], default='send', max_length=8),
        ),
    ]