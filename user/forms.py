from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import ProfileModel

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('user', 'status', 'created_on', 'updated_on')