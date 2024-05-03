from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


def loginPage(request):
   # if request.user.is_authenticated:
        ##return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            ##return redirect('index')
        else:
            messages.info(request, 'USERNAME or PASSWORD is incorrect')

    context = {"title": "login"}
    return render(request, 'login.html', context)




def register(request):
    #if request.user.is_authenticated:
        #return redirect('index')

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()


            user = form.cleaned_data.get('username')


            messages.success(request, 'Account ' + user + ' was created')

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
        user = User.objects.get(username=profile.user)

        if user == request.user:
            is_your_profile = True
        else:
            is_your_profile = False

        context = {"user": user, "profile": profile,"exist": True, "is_your_profile": is_your_profile}
    except Profile.DoesNotExist:
        context = {"exist": False}
    return render(request, 'profiles/profile.html', context)


@login_required(login_url='login')
def changeProfile(request):


    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profiles/change_profile.html', {'user_form': user_form, 'profile_form': profile_form})

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


