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
from Users.models import PreferenceList
from Songs.models import Song
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.dispatch import receiver
from django.http import HttpResponse
from .forms import ArtistForm


@login_required(login_url="login")
def create_artist(request):
    artist = Artist.objects.filter(profile=request.user.profile)
    if artist.exists():
        #messages.error(request, 'Artist already exists')

        return render(request, 'create_artist.html',
                      {'exist': True, 'artist': artist})

    if request.method == 'POST':



        artist_form = ArtistForm(request.POST,request.FILES)

        if artist_form.is_valid():
            new_artist = artist_form.save(commit=False)

            new_artist.profile = request.user.profile
            new_artist.save()  # Save the new song first

            #messages.success(request, 'Artis has been created successfully')
            return redirect('/artist/' + new_artist.slug)
    else:
        artist_form = ArtistForm()

    return render(request, 'create_artist.html',
                  {'artist_form': artist_form, 'exist' : False })

@login_required(login_url="login")
def artist_profile(request, artist_id):
    try:
        artist = Artist.objects.get(slug=artist_id)
        profile = artist.profile
        prlist = PreferenceList.objects.get(profile=request.user.profile)




        if profile.user == request.user:
            is_your_profile = True
        else:
            is_your_profile = False

        print(artist, prlist.artists.all())
        if artist in prlist.artists.all():
            you_are_follower = True
        else:
            you_are_follower = False

        temp = False
        songs = []
        for instance in Song.objects.all():
            for field in instance._meta.many_to_many:
                if field == artist:
                    songs.append(instance)
                    break
        #print(songs)

        context = {"user": profile.user, "artist": artist,
                   "exist": True, "is_your_profile": is_your_profile,"you_are_follower": you_are_follower,
                   "songs": songs, 'songs_num': len(songs)}

    except Artist.DoesNotExist:
        context = {"exist": False}
    return render(request, 'artist_profile.html', context)


@login_required(login_url='login')
def artist_change(request):
    try:
        artist = Artist.objects.get(profile=request.user.profile)
        artist_form = ArtistForm(request.POST, request.FILES, instance=artist)

        if request.method == 'POST':


            if artist_form.is_valid():
                artist_form.save()
                messages.success(request, 'This artist has been changed successfully')
                return redirect('/artist/' + artist.slug)
        else:
            artist_form = ArtistForm()

        return render(request, 'create_artist.html',
                  {'artist_form': artist_form, 'exist': False})
    except Artist.DoesNotExist:
        return render(request, 'not_found.html', {'what': 'artist'})



@login_required(login_url='login')
def artist_delete(request):
    try:
        artist = Artist.objects.get(profile=request.user.profile)
        artist.delete()

        messages.success(request, 'This artist has been deleted successfully')
        return redirect(request.path_info)
    except Artist.DoesNotExist:
        return render(request, 'not_found.html', {'what': 'artist'})

@login_required(login_url='login')
def follow_artist(request, artist_id):
    try:
        artist = Artist.objects.get(slug=artist_id)
        prlist = PreferenceList.objects.get(profile=request.user.profile)

        prlist.artists.add(artist)

        messages.success(request, 'You are follower of this artist now')
        return redirect('../../artist/' + artist_id)
    except Artist.DoesNotExist:
        return render(request, 'not_found.html', {'what': 'artist'})


@login_required(login_url='login')
def unfollow_artist(request, artist_id):
    try:
        artist = Artist.objects.get(slug=artist_id)
        prlist = PreferenceList.objects.get(profile=request.user.profile)

        prlist.artists.remove(artist)

        messages.success(request, 'You are not follower of this artist now')
        return redirect('../../artist/' + artist_id)
    except Artist.DoesNotExist:
        return render(request, 'not_found.html', {'what': 'artist'})

