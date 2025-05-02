from django.urls import path
from .views import index, doctor_detail

urlpatterns = [
    path('', index, name='listings_index'),
    path('doctor/<int:pk>/', doctor_detail, name='doctor_detail'),
]
# Compare this snippet from Backend%20Code%20%28Django%29/Users%20Module/urls.py:
# from django.urls import path
# from .views import register, login_view, logout_view, profile
# from django.contrib.auth import views as auth_views