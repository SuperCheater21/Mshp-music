from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, PreferenceList
from Genres.models import Genre


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)

    class Meta:
        model = Profile
        fields = ['image', 'bio','first_name','last_name']


class PreferencesSetForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        label='Your favourite genre',
        queryset= Genre.objects.all(),
    )
    class Meta:
        model = PreferenceList
        fields = ['genres']
