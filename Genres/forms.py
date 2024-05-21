from django import forms
from .models import Genre


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Genre
        fields = ['name']
