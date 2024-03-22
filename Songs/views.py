from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import  login_required

from django.contrib.auth import authenticate, login, logout


def music_page(request):
    song = Song(title='Paranoid Android', artist='Radiohead')
    song.save()
    context = {'song': song}
    return render(request, 'music_page.html', context)