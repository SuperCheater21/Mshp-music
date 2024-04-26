from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
#from .models import Friend
#from .forms import AddFriendsForm, DeleteFriendsForm
from django.contrib.auth import authenticate, login, logout


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

    context = {}
    return render(request, 'login.html', context)


def restore(request):
    return render(request, 'restore.html')


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

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return render(request, 'logout.html')



