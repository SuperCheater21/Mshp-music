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
from .forms import SongUploadForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver



def song_list(request):
    songs = Song.objects.all()  # Fetch all songs
    return render(request, 'music/song_list.html', {'songs': songs})

@login_required(login_url='login')
def play_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)  # Get song by ID
    first_element = Song.objects.order_by('id').first().id
    last_element = Song.objects.order_by('id').last().id
    next_element = song_id + 1 if song_id < last_element else first_element
    prev_element = song_id - 1 if song_id > first_element else last_element
    context = {'song': song,
               'next_song_id': next_element,
               'prev_song_id': prev_element,
               }
    return render(request, 'play_song.html', context)

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


            new_song.artists.add(request.user.profile)
            new_song.album = Playlist.objects.get(slug=playlist_id)

            new_song.save()
            messages.success(request, 'This song is added successfully')
            #return redirect('../profile/' + request.user.profile.slug)
    else:
        song_form = SongUploadForm()

    return render(request, 'upload_song.html',
                  {'song_form': song_form})



