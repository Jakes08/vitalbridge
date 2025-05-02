from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

@login_required
def messaging(request):
    # Placeholder for secure messaging; implement real-time chat with Django Channels later
    return render(request, 'messaging/messaging.html')
