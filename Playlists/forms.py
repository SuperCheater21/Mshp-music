from django import forms
from .models import Playlist


class PlaylistForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    playlist_thumbnail = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    is_private = forms.BooleanField(required=False)

    class Meta:
        model = Playlist
        fields = ['title', 'playlist_thumbnail', 'genre', 'is_private']
