from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from authentication.forms import LoginForm, SignupForm
from twitter_user.models import TwitterUser
from tweet.models import Tweet

# Create your views here.

def home_view(request):
    tweets = Tweet.objects.all().order_by('-time_posted')
    following = request.user.following.all()
    follow_count = (request.user.following.all().count() - 1)

    return render(request, 'home.html', {'tweets': tweets, 'following': following, 'follow_count': follow_count})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweeter = authenticate(request,
                username = data.get('username'),
                password = data.get('password')
            )
            if tweeter:
                login(request, tweeter)
                return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweeter = TwitterUser.objects.create_user(
                username = data.get('username'),
                displayname = data.get('displayname'),
                password = data.get('password')
            )
            if new_tweeter:
                login(request, new_tweeter)
                return HttpResponseRedirect(reverse('homepage'))
    
    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

