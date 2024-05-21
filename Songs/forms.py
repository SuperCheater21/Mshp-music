from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    song_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    audio_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    # audio_file =
    lyrics = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Song
        fields = ['song_name', 'thumbnail', 'audio_file', 'lyrics']
