from django.core.paginator import Paginator
from .models import Song
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404
from .models import Song
from Playlists.models import Playlist
from Artists.models import Artist
from .forms import SongUploadForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver



def song_list(request):
    songs = Song.objects.all()  # Fetch all songs
    return render(request, 'music/song_list.html', {'songs': songs})

@login_required(login_url='login')
def play_song_by_slug(request, song_id):
    song = get_object_or_404(Song, slug=song_id)  # Get song by ID
    context = {'song': song}
    return render(request, 'play_song_by_slug.html', context)

@login_required(login_url='login')
def play_song_in_playlist(request,playlist_id, song_id):
    playlist = get_object_or_404(Playlist, slug=playlist_id)

    prev_element = song_id - 1
    next_element = song_id + 1

    if prev_element < 0:
        prev_element = len(playlist.songs.all()) - 1
    if next_element >= len(playlist.songs.all()):
        next_element = 0
    #print(playlist.songs.all())
    song = playlist.songs.all()[song_id]

    context = {'song': song,
               'prev_song_id':prev_element,
               'next_song_id':next_element}
    return render(request, 'play_song_in_playlist.html', context)





@login_required(login_url='login')
def music_page(request):

    return render(request, 'music/music_page.html')

@login_required(login_url='login')
def my_vibe_page(request):
    pass

@login_required(login_url='login')
def upload_song(request, playlist_id):
    if request.method == 'POST':
        song_form = SongUploadForm(request.POST,request.FILES)

        if song_form.is_valid():
            new_song = song_form.save(commit=False)
            playlist = Playlist.objects.get(slug=playlist_id)
            new_song.save()  # Save the new song first

            playlist.songs.add(new_song)
            new_song.artists.add(get_object_or_404(Artist, profile=request.user.profile))

            messages.success(request, 'This song is added successfully')
            song_id = len(playlist.songs.all()) - 1
            return redirect('play/'  + str(song_id))
    else:
        song_form = SongUploadForm()

    return render(request, 'upload_song.html',
                  {'song_form': song_form})



