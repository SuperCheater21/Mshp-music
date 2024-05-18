from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404
from .models import Playlist
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import PlaylistCreationForm


@login_required(login_url='login')
def create_playlist(request):
    if request.method == 'POST':
        playlist_form = PlaylistCreationForm(request.POST,request.FILES)

        if playlist_form.is_valid():
            new_playlist= playlist_form.save(commit=False)


            new_playlist.author = request.user.profile

            new_playlist.save()
            messages.success(request, 'This playlist is created successfully')
            return redirect('../playlist/' + new_playlist.slug)
    else:
        playlist_form = PlaylistCreationForm()

    return render(request, 'create_playlist.html',
                  {'playlist_form': playlist_form})

