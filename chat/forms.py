from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.shortcuts import render, HttpResponse, redirect


class FindUserForm(forms.ModelForm):
    user =  forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control find_user_form',
        'placeholder':'Find User'}
    ))

    class Meta:
        model = User
        fields = ('user',)
