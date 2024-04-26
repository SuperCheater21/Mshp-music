from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Friend


class AddFriendsForm(forms.Form):
    friend = forms.ModelChoiceField(queryset=User.objects.all(), label='Select a friend')

    def __init__(self, user, *args, **kwargs):
        super(AddFriendsForm, self).__init__(*args, **kwargs)
        self.fields['friend'].queryset = User.objects.exclude(id=user.id)


class DeleteFriendsForm(forms.Form):
    friend = forms.ModelChoiceField(queryset=Friend.objects.none(), label='Select a friend')

    def __init__(self, user, *args, **kwargs):
        super(DeleteFriendsForm, self).__init__(*args, **kwargs)
        self.fields['friend'].queryset = user.list_of_friends.all()


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']