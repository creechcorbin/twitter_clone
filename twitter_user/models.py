from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TwitterUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    notifications = models.IntegerField(default=0)
    num_of_tweets = models.IntegerField(default=0)
    following = models.ManyToManyField('self', symmetrical=False)
    
