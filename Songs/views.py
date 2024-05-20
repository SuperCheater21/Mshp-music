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


def song_list(request):
    songs = Song.objects.all()  # Fetch all songs
    return render(request, 'song_list.html', {'songs': songs})


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

def music_page(request):
    song = Song(title='Paranoid Android', artist='Radiohead')
    song.save()
    context = {'song': song}
    return render(request, 'music_page.html', context)