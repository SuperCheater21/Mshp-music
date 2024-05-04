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
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import FriendRequest, FriendList
from Users.models import Profile

@login_required(login_url='login')
def send_request(request,profile_id):
    sender_user = request.user.profile
    receiver_user = Profile.objects.get(slug=profile_id)

    friend_request = FriendRequest.objects.get_or_create(sender=sender_user,receiver=receiver_user)
    return redirect('../' + profile_id)

@login_required(login_url='login')
def accept_request(request,profile_id):
    sender_user = request.user.profile
    receiver_user = Profile.objects.get(slug=profile_id)

    try:
        friend_request = FriendRequest.objects.get(sender=sender_user,receiver=receiver_user)
        friend_request.status = 'accepted'
        friend_request.save()
    except FriendRequest.DoesNotExist:
        pass
    return redirect('../' + profile_id)

@login_required(login_url='login')
def reject_request(request,profile_id):
    sender_user = request.user.profile
    receiver_user = Profile.objects.get(slug=profile_id)

    try:
        friend_request = FriendRequest.objects.get(sender=sender_user, receiver=receiver_user)
        friend_request.status = 'rejected'
        friend_request.save()
    except FriendRequest.DoesNotExist:
        pass
    return redirect('../' + profile_id)


@login_required(login_url='login')
def delete_friend(request,profile_id):
    target_profile = Profile.objects.get(slug=profile_id)

    target_friend_list = FriendList.objects.get(profile=target_profile)
    user_friend_list = FriendList.objects.get(profile=request.user.profile)

    target_friend_list.friends.remove(request.user.profile)
    user_friend_list.friends.remove(target_profile)

    target_profile.save()
    user_friend_list.save()

    return redirect('../' + profile_id)


@receiver(post_save, sender=FriendRequest)
def post_save_interaction_with_friend_request(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
#print("here")
    if instance.status == 'accepted':
        #print('accepted')
        try:
            friend_list_sender = FriendList.objects.get(profile=sender_)
            friend_list_receiver = FriendList.objects.get(profile=receiver_)

            friend_list_sender.friends.add(receiver_)
            friend_list_receiver.friends.add(sender_)

            friend_list_sender.save()
            friend_list_receiver.save()
            FriendRequest.objects.filter(pk=instance.pk).delete()
        except FriendRequest.DoesNotExist:
            pass

    elif instance.status == 'rejected':
        #print('rejected')
        FriendRequest.objects.filter(pk=instance.pk).delete()





