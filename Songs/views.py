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
    # Logic to handle song playback using JavaScript or a third-party player library
    # (implementation details depend on your chosen approach)
    context = {'song': song}
    return render(request, 'play_song.html', context)
