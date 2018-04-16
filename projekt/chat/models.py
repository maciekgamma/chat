from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conversations(models.Model):
    name = models.CharField(max_length=20)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Participants(models.Model):
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

class Messages(models.Model):
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    message =  models.CharField(max_length=100)
    sent_time = models.DateTimeField(auto_now_add=True)

class Friends(models.Model):
    user_one = models.ForeignKey(User, related_name="first_user", on_delete=models.CASCADE)
    user_two = models.ForeignKey(User, related_name="second_user", on_delete=models.CASCADE)
