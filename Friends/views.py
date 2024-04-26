from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
#from Friends.models import FriendRequest
@login_required(login_url='login')
def send_friend_req(request, *args, **kwargs):
    user = request.user
    payload= {}

    if request.method == "POST":
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = User.objects.get(pk=user_id)


