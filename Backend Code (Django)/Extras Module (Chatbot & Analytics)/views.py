from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

@login_required
def chatbot_triage(request):
    # Placeholder for an AI-based chatbot triage (e.g., Dialogflow integration)
    return render(request, 'extras/chatbot.html')

@login_required
def analytics_dashboard(request):
    # Placeholder for an analytics dashboard (to be enhanced with Chart.js or Plotly)
    return render(request, 'extras/analytics_dashboard.html')
