from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Relationship



@receiver(post_save, sender=Relationship)
def post_save_interaction_with_friend_request(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver

    if instance.status == 'accepted':
        sender_.friends.add(receiver_.profile)
        receiver_.friends.add(sender_.profile)

        sender_.save()
        receiver_.save()

    elif instance.status == 'rejected':
        Relationship.objects.filter(pk=instance.pk).delete()



