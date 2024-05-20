from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404
from .models import Playlist
from Artists.models import Artist
from Users.models import Profile
from Songs.models import Song
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import PlaylistForm
from django.http import HttpResponse

@login_required(login_url='login')
def create_playlist(request):
    if request.method == 'POST':
        playlist_form = PlaylistForm(request.POST,request.FILES)

        if playlist_form.is_valid():
            new_playlist= playlist_form.save(commit=False)


            new_playlist.author = request.user.profile

            new_playlist.save()
            messages.success(request, 'This playlist has been  created successfully')
            return redirect('../playlist/' + new_playlist.slug)
    else:
        playlist_form = PlaylistForm()

    return render(request, 'create_playlist.html',
                  {'playlist_form': playlist_form})

@login_required(login_url='login')
def change_playlist(request, playlist_id):
    try:
        playlist_form = PlaylistForm(request.POST, request.FILES, instance=Playlist.objects.get(slug=playlist_id))
        if request.method == 'POST':


            if playlist_form.is_valid():
                playlist_form.save()
                messages.success(request, 'This playlist has been changed successfully')
                return redirect('/playlist/' + playlist_id)
        else:
            playlist_form = PlaylistForm()

        return render(request, 'create_playlist.html',
                  {'playlist_form': playlist_form})
    except Playlist.DoesNotExist:
        return render(request, 'not_found.html', {'what': 'playlist'})



@login_required(login_url='login')
def delete_playlist(request, playlist_id):
    try:
        playlist = Playlist.objects.get(slug=playlist_id)
        playlist.delete()

        messages.success(request, 'This playlist has been deleted successfully')
        return redirect(request.path_info)
    except Playlist.DoesNotExist:
        return render(request, 'not_found.html', {'what': 'playlist'})


@login_required(login_url='login')
def playlist_page(request, playlist_id):
    try:
        playlist = Playlist.objects.get(slug=playlist_id)
        profile = playlist.author




        if profile.user == request.user:
            is_your_playlist = True
        else:
            is_your_playlist = False


        songs = playlist.songs.all();
        temp = []

        for song in songs:
            for artist in song.artists.all():
                temp.append(artist)

        temp = set(temp)
        artists = list(temp)
        context = {"profile": profile, "playlist" : playlist, "artists" : artists,
                   "exist": True, "is_your_playlist": is_your_playlist, "songs" : songs}

    except Playlist.DoesNotExist:
        context = {"exist": False}
    return render(request, 'playlist_page.html', context)


