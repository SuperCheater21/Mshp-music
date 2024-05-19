from django import forms
from .models import Artist


class ArtistCreationForm(forms.ModelForm):
    stage_name = forms.CharField(max_length=50,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    #audio_file =
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)

    class Meta:
        model = Artist
        fields = ['stage_name','description']
