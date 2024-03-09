from django.core.paginator import Paginator
from .models import Song
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


def music_page(request):
    paginator = Paginator(Song.object.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, 'music_page.html', context)
