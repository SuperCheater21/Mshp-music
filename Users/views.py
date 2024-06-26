from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PreferencesSetForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from Friends.models import FriendList, FriendRequest
from Playlists.models import Playlist
from Songs.models import Song
from .models import Profile, PreferenceList
from django.db import IntegrityError

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('../')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)


            return redirect('../')
        else:
            messages.info(request, 'USERNAME or PASSWORD is incorrect')

    context = {"title": "login"}
    return render(request, 'login.html', context)




def register(request):
    if request.user.is_authenticated:
        return redirect('../')

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()


            username = form.cleaned_data.get('username')


            messages.success(request, 'Account ' + username + ' was created')

            return redirect('login')

    context = {'form': form, "title": "register"}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return render(request, 'logout.html')

@login_required(login_url='login')
def profilePage(request, profile_id):
    try:
        profile = Profile.objects.get(slug=profile_id)
        #user = User.objects.get(username=profile.user)

        is_your_friend = False
        is_your_profile = False
        is_friend_request_sent = False
        is_sender = False
        is_receiver = False

        if profile.user == request.user:
            is_your_profile = True
        else:

            your_friendlist = get_object_or_404(FriendList, profile=request.user.profile)

            if your_friendlist.friends.filter(user=profile).exists():
                is_your_friend = True
            else:

                if FriendRequest.objects.filter(sender=profile, receiver=request.user.profile).exists():
                    is_receiver = True
                elif FriendRequest.objects.filter(sender=request.user.profile, receiver=profile).exists():
                    is_sender = True



        genres = PreferenceList.objects.get(profile=profile)
        context = {"user": profile.user, "profile": profile,
                   "exist": True, "is_your_profile": is_your_profile,
                   "genres": genres, "is_your_friend": is_your_friend,
                   "is_receiver": is_receiver, "is_sender": is_sender, "genre_num": len(genres.genres.all())}

    except Profile.DoesNotExist:
        return render(request, 'not_found.html')
    return render(request, 'profiles/profile.html', context)


@login_required(login_url='login')
def changeProfile(request):


    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('../profile/' + request.user.profile.slug)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profiles/change_profile.html', {'user_form': user_form, 'profile_form': profile_form, 'user': request.user})

@login_required(login_url='login')
def update_profile_preferences(request):
    if request.method == 'POST':
        pr_list = get_object_or_404(PreferenceList, profile=request.user.profile)

        preference_form = PreferencesSetForm(request.POST, request.FILES,instance=pr_list)
        if preference_form.is_valid():
            preference_form.save()
            messages.success(request, 'Your profile preferences have been updated successfully')
            return redirect('../' + request.user.profile.slug)
    else:
        preference_form = PreferencesSetForm()
    return render(request, 'profiles/change_preferences.html', {'preference_form': preference_form, 'user': request.user})

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        prlist = PreferenceList.objects.create(profile=instance.profile)
        FriendList.objects.create(profile=instance.profile)
        try:
            Playlist.objects.create(title="Your favourite",
                                    author=instance.profile,
                                    playlist_thumbnail='playlist_pics/heart.jpeg',
                                    is_private=True, genre="all sorts of genres")
        except IntegrityError:
            pl = Playlist.objects.get(author=instance.profile)
            prlist.playlists.add(pl)




@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@login_required(login_url='login')
def show_profile_preferences_artists(request, profile_id):
    try:
        profile = Profile.objects.get(slug=profile_id)
        prlist = profile.preferencelist #PreferenceList.objects.get(profile=profile)

        if profile == request.user.profile:
            is_your_profile = True
        else:
            is_your_profile = False

        exist = False
        if len(prlist.get_artists()) > 0:
            exist = True

        return render(request, 'profiles/show_artist_preferences.html',
                      {"artists": prlist.get_artists(), "is_your_profile":is_your_profile, "profile": profile, "exist": exist})
    except Profile.DoesNotExist:
        return render(request, 'not_found.html')


@login_required(login_url='login')
def show_profile_preferences_playlists(request, profile_id):
    try:
        profile = Profile.objects.get(slug=profile_id)
        prlist = profile.preferencelist  # PreferenceList.objects.get(profile=profile)

        if profile == request.user.profile:
            is_your_profile = True
        else:
            is_your_profile = False

        exist = False
        if len(prlist.get_playlists()) > 0:
            exist = True



        return render(request, 'profiles/show_playlists_preferences.html',
                      {"playlists": prlist.get_playlists(), "is_your_profile": is_your_profile, "profile": profile, "exist": exist})
    except Profile.DoesNotExist:
        return render(request, 'not_found.html')

@login_required(login_url='login')
def mainPage(request):
    prlist = request.user.profile.preferencelist

    return render(request, 'main.html', {"user": request.user,"users": User.objects.all(), "genres":prlist.get_genres(), 'users_num': len(User.objects.all()), "genres_num":  len(prlist.get_genres()),"songs": Song.objects.all(), "songs_num": len(Song.objects.all()), "playlists": Playlist.objects.all(), "playlists_num": len(Playlist.objects.all())})