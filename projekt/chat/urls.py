from django.urls import path
from . import views
from accounts.forms import CustomAuthForm
from chat.views import HomeView

app_name='chat'

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
]
