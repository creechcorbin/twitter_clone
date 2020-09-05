from django.db import models
from tweet.models import Tweet
from twitter_user.models import TwitterUser

# Create your models here.

class Notification(models.Model):
    notifying_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, default=None)
    user_notified = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, default=None)
    read_status = models.BooleanField(default=False)