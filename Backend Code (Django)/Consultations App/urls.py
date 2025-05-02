from django.urls import path
from .views import appointment, consultation, feedback, ehr_lookup

urlpatterns = [
    path('book/', appointment, name='appointment'),
    path('consult/', consultation, name='consultation'),
    path('ehr/', ehr_lookup, name='ehr_lookup'),
    path('feedback/<int:appointment_id>/', feedback, name='feedback'),
]
