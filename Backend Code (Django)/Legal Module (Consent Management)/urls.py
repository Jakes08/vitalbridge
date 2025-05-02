from django.urls import path
from .views import consent_form

urlpatterns = [
    path('consent/', consent_form, name='consent'),
]
