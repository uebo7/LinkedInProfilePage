from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about_me = models.CharField(max_length=350)
    current_position = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

