from django.db import models
from twitter_user.models import TwitterUser

# Create your models here.

class Tweet(models.Model):
    body = models.CharField(max_length=140)
    tweeter = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    time_posted = models.DateTimeField()
