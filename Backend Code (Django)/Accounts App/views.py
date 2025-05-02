import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.save()
                messages.success(request, _("Registration successful. Please check your email for verification (stub) and log in."))
                return redirect('login')
            except Exception as e:
                logger.error("Registration error: %s", e)
                messages.error(request, _("An error occurred during registration."))
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            try:
                user = form.get_user()
                login(request, user)
                messages.success(request, _("Logged in successfully."))
                return redirect('dashboard')
            except Exception as e:
                logger.error("Login error: %s", e)
                messages.error(request, _("An error occurred during login."))
        else:
            messages.error(request, _("Invalid username or password."))
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, _("You have been logged out."))
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        try:
            request.user.email = request.POST.get('email')
            request.user.full_name = request.POST.get('full_name')
            request.user.phone = request.POST.get('phone')
            request.user.save()
            messages.success(request, _("Profile updated successfully."))
            return redirect('profile')
        except Exception as e:
            logger.error("Profile update error: %s", e)
            messages.error(request, _("Unable to update profile at this time."))
    return render(request, 'accounts/profile.html')

@login_required
def dashboard(request):
    try:
        if request.user.role == 'doctor':
            template = 'accounts/dashboard_doctor.html'
        else:
            template = 'accounts/dashboard_patient.html'
        return render(request, template)
    except Exception as e:
        logger.error("Dashboard error: %s", e)
        messages.error(request, _("An error occurred loading the dashboard."))
        return redirect('login')
