from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    age = models.IntegerField()
    devlang = models.CharField(max_length=64, default=None)
    books = models.CharField(max_length=128, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')