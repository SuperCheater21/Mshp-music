from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404
from .models import Artist
from Playlists.models import Playlist
from Songs.models import Song
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.dispatch import receiver
from django.http import HttpResponse
from .forms import ArtistCreationForm


@login_required(login_url="login")
def create_artist(request):
    exist = False
    if request.method == 'POST':
        artist = Artist.objects.filter(profile=request.user.profile)
        if artist.exists():
            messages.error(request, 'Artist already exists')

            return render(request, 'create_artist.html',
                          {'exist' : True, 'artist' : artist})


        artist_form = ArtistCreationForm(request.POST,request.FILES)

        if artist_form.is_valid():
            new_artist = artist_form.save(commit=False)

            new_artist.profile = request.user.profile
            new_artist.save()  # Save the new song first

            #messages.success(request, 'Artis has been created successfully')
            return redirect('../artist/' + new_artist.slug)
    else:
        artist_form = ArtistCreationForm()

    return render(request, 'create_artist.html',
                  {'artist_form': artist_form, 'exist' : exist })

@login_required(login_url="login")
def artist_profile(request, artist_id):
    try:
        artist = Artist.objects.get(slug=artist_id)
        profile = artist.profile




        if profile.user == request.user:
            is_your_profile = True
        else:
            is_your_profile = False

        temp = False
        songs = []
        for instance in Song.objects.all():
            for field in instance._meta.many_to_many:
                if field == artist:
                    songs.append(instance)
                    break

        context = {"user": profile.user, "artist": artist,
                   "exist": True, "is_your_profile": is_your_profile,
                   "songs": songs}

    except Artist.DoesNotExist:
        context = {"exist": False}
    return render(request, 'artist_profile.html', context)
