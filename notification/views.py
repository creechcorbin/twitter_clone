from django.shortcuts import render
from notification.models import Notification

# Create your views here.

def notification_view(request):
    notifications = Notification.objects.all()
    follow_count = (request.user.following.all().count() - 1)
    unread = []

    for notification in notifications:
        if notification.read_status == False:
            unread.append(notification)
            notification.read_status = True
            notification.save()

    return render(request, 'notifications.html', {'unread': unread, 'follow_count': follow_count})
