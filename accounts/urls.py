from django.urls import path
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)
from accounts.forms import CustomAuthForm


app_name='accounts'

urlpatterns = [
    path('login/', login, name='login',
    kwargs={'authentication_form':CustomAuthForm,
    'template_name':'accounts/login.html'}),
    path('logout/', logout, name='logout', kwargs={'next_page':'/accounts/login/'}),
    path('register/', views.register, name='register'),

]
