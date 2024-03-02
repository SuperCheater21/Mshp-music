from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import  login_required

from django.contrib.auth import authenticate, login, logout


