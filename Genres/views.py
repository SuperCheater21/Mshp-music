from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .models import Genre
from .forms import GenreForm


@login_required(login_url='login')
def create_genre(request):
    try:
        if request.method == 'POST':
            genre_form = GenreForm(request.POST)

            if genre_form.is_valid():
                genre_form.save()
                messages.success(request, 'This genre has been added successfully')
                return redirect("/")
        else:
            genre_form = GenreForm()

        return render(request, 'create_genre.html',
                      {'genre_form': genre_form, 'exist': False})
    except Genre.DoesNotExist:
        pass
