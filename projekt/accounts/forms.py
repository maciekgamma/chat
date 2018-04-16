from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.shortcuts import render, HttpResponse, redirect


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control', 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control', 'placeholder': 'Password'}))



# stare
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
    'class':'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control', 'placeholder': 'Login'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control', 'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control', 'placeholder': 'Last name'}))

    class Meta:
        model = User
        fields=(
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        )
def save(self, commit=True):
    user= super(RegistrationForm, self).save(commit=False)
    user.first_name = cleaned_data['first_name']
    user.last_name = cleaned_data['last_name']
    user.email = cleaned_data['email']

    if commit:
        user.save()
    return user
class EditProfileForm(UserChangeForm):

    class Meta:
        model=User
        fields =(
            'email',
            'first_name',
            'last_name',
            'password'
        )
