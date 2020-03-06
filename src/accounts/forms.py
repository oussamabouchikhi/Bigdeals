from django import forms
from . import models
from django.contrib.auth.models import User


"""
user info are in two models (django User & our custom user profile)
so we want to create a form which includes both
"""
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = ['image', 'country', 'address']
