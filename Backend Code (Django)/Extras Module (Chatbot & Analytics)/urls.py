from django.urls import path
from .views import chatbot_triage, analytics_dashboard

urlpatterns = [
    path('chatbot/', chatbot_triage, name='chatbot'),
    path('analytics/', analytics_dashboard, name='analytics_dashboard'),
]
