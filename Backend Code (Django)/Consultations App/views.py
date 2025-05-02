import logging, os, requests
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from .forms import AppointmentForm, FeedbackForm
from .models import Appointment, ConsultationFeedback

logger = logging.getLogger(__name__)

@login_required
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            try:
                appt = form.save(commit=False)
                appt.patient = request.user
                appt.save()
                messages.success(request, _("Appointment booked successfully!"))
                return redirect('appointment')
            except Exception as e:
                logger.error("Error saving appointment: %s", e)
                messages.error(request, _("Failed to book appointment."))
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = AppointmentForm()
    return render(request, 'consultations/appointment.html', {'form': form})

@login_required
def consultation(request):
    try:
        token = AccessToken(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_API_KEY'), os.getenv('TWILIO_API_SECRET'), identity=request.user.username)
        video_grant = VideoGrant(room='ConsultRoom')
        token.add_grant(video_grant)
        twilio_token = token.to_jwt().decode('utf-8')
    except Exception as e:
        logger.error("Error generating Twilio token: %s", e)
        twilio_token = None
        messages.error(request, _("Video consultation service is currently unavailable."))
    return render(request, 'consultations/consultation.html', {'twilio_token': twilio_token})

@login_required
def ehr_lookup(request):
    try:
        response = requests.get(f"{os.getenv('EHR_API_URL', 'https://api.exampleehr.com/patientrecords')}?user={request.user.username}", timeout=5)
        response.raise_for_status()
        ehr_data = response.json()
    except Exception as e:
        logger.error("EHR lookup error: %s", e)
        ehr_data = {}
        messages.error(request, _("Failed to retrieve EHR data."))
    return render(request, 'consultations/ehr_lookup.html', {'ehr_data': ehr_data})

@login_required
def feedback(request, appointment_id):
    appt = get_object_or_404(Appointment, id=appointment_id, patient=request.user)
    try:
        feedback_obj = appt.consultationfeedback
    except ConsultationFeedback.DoesNotExist:
        feedback_obj = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback_obj)
        if form.is_valid():
            try:
                fb = form.save(commit=False)
                fb.appointment = appt
                fb.save()
                messages.success(request, _("Feedback submitted successfully."))
                return redirect('dashboard')
            except Exception as e:
                logger.error("Feedback error: %s", e)
                messages.error(request, _("Failed to submit feedback."))
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = FeedbackForm(instance=feedback_obj)
    return render(request, 'consultations/feedback.html', {'form': form, 'appointment': appt})
