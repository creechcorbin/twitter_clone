from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from twitter_user.models import TwitterUser
from notification.models import Notification
from tweet.forms import TweetForm
from datetime import datetime
import re


# Create your views here.

def post_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                body = data.get('body'),
                time_posted = datetime.now(),
                tweeter = request.user
            )
            mentions = re.findall(r'@(\w+)', data.get('body'))
            if mentions:
                users = TwitterUser.objects.all()
                for mention in mentions:
                    if TwitterUser.objects.get(username=mention):
                        Notification.objects.create(
                            notifying_tweet = new_tweet,
                            user_notified = TwitterUser.objects.get(username=mention)
                        )
            if new_tweet:
                tweeter = request.user
                tweeter.num_of_tweets += 1
                tweeter.save()
                return HttpResponseRedirect(reverse('homepage'))

    form = TweetForm()
    return render(request, 'generic_form.html', {'form': form})

def tweet_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)

    return render(request, 'tweet_detail.html', {'tweet': tweet})