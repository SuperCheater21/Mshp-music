from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from .models import Friend
from .forms import AddFriendsForm, DeleteFriendsForm
from django.contrib.auth import authenticate, login, logout


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'USERNAME or PASSWORD is incorrect')

    context = {}
    return render(request, 'login.html', context)


def restore(request):
    return render(request, 'restore.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account ' + user + ' was created')

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return render(request, 'logout.html')


@login_required
def add_friend(request):
    if request.method == 'POST':
        form = AddFriendsForm(request.user, request.POST)
        if form.is_valid():
            friend = form.cleaned_data['friend']
            friend_obj, created = Friend.objects.get_or_create(user=request.user)
            friend_obj.list_of_friends.add(friend)
            return render(request, 'success.html', {'message': f'{friend.username} added to your friends list'})
    else:
        form = AddFriendsForm(request.user)

    return render(request, 'add_friend.html', {'form': form})

@login_required(login_url='login')
def delete_friend(request):
    if request.method == 'POST':
        form = DeleteFriendsForm(request.user, request.POST)
        if form.is_valid():
            friend_to_delete = form.cleaned_data['friend']
            request.user.list_of_friends.remove(friend_to_delete)
            return render(request, 'success.html', {'message': f'{friend_to_delete.username} removed from your friends list'})
    else:
        form = DeleteFriendsForm(request.user)

    return render(request, 'delete_friend.html', {'form': form})

