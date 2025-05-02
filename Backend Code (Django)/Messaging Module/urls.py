from django.urls import path
from .views import messaging

urlpatterns = [
    path('', messaging, name='messaging'),
]
