from django import forms

from django.contrib.auth.models import User
from .models import UserProfile


class UserCreateForm(forms.ModelForm):

    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"class": "username form-control", "placeholder":"Username"})
    )

    email = forms.CharField(
        label='',
        widget=forms.EmailInput(attrs={"class": "email form-control", "placeholder":"Email"})
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"class": "password form-control", "placeholder":"Password"})
    )
    
    class Meta:
        model = User

        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    
    profile_pic = forms.FileField(
        label="Profile Picture",
        widget=forms.FileInput(attrs={"class":"profile_pic_upload"})
    )

    class Meta:
        model = UserProfile

        fields = ['profile_pic',]
