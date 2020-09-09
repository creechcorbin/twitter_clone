from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from twitter_user.models import TwitterUser

# Create your views here.

def profile_view(request, user_name):
    tweets = Tweet.objects.all().order_by('-time_posted')
    selected_user = TwitterUser.objects.get(username=user_name)
    following = request.user.following.all()
    follow_count = (request.user.following.all().count() - 1)
    sel_follow_count = (selected_user.following.all().count() - 1)

    return render(request, 'profile.html', {'selected_user': selected_user, 'tweets': tweets, 'following': following, 'follow_count': follow_count, 'sel_follow_count': sel_follow_count})

def follow_view(request, user_id):
    user = request.user
    selected_user = TwitterUser.objects.get(id=user_id)
    
    user.following.add(selected_user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow_view(request, user_id): 
    user = request.user
    selected_user = TwitterUser.objects.get(id=user_id)
    
    user.following.remove(selected_user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))