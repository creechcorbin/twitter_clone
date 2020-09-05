"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import home_view, login_view, signup_view, logout_view
from tweet.views import post_tweet_view, tweet_view
from twitter_user.views import profile_view, follow_view, unfollow_view
from notification.views import notification_view

urlpatterns = [
    path('', home_view, name='homepage'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('addtweet/', post_tweet_view, name='post'),
    path('notifications/', notification_view, name='notifications'),
    path('follow/<str:user_id>/', follow_view),
    path('unfollow/<str:user_id>/', unfollow_view),
    path('admin/', admin.site.urls),
    path('<str:user_name>/', profile_view, name='profile'),
    path('tweet/<int:tweet_id>', tweet_view, name='tweetdeet'),
]
