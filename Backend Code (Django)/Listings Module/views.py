from django.shortcuts import render, get_object_or_404
from .models import DoctorListing, Hospital
from django.utils.translation import gettext as _

def index(request):
    doctors = DoctorListing.objects.order_by('-rating')[:5]
    hospitals = Hospital.objects.order_by('-rating')[:5]
    return render(request, 'listings/index.html', {'doctors': doctors, 'hospitals': hospitals})

def doctor_detail(request, pk):
    doctor = get_object_or_404(DoctorListing, pk=pk)
    return render(request, 'listings/details.html', {'doctor': doctor})
def hospital_detail(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'listings/hospital_details.html', {'hospital': hospital})
def search(request):
    query = request.GET.get('q')
    if query:
        doctors = DoctorListing.objects.filter(name__icontains=query)
        hospitals = Hospital.objects.filter(name__icontains=query)
    else:
        doctors = DoctorListing.objects.none()
        hospitals = Hospital.objects.none()
    return render(request, 'listings/search_results.html', {'doctors': doctors, 'hospitals': hospitals})
def filter_by_specialty(request):
    specialty = request.GET.get('specialty')
    if specialty:
        doctors = DoctorListing.objects.filter(specialty__icontains=specialty)
    else:
        doctors = DoctorListing.objects.all()
    return render(request, 'listings/specialty_filter.html', {'doctors': doctors})
def filter_by_location(request):
    location = request.GET.get('location')
    if location:
        hospitals = Hospital.objects.filter(location__icontains=location)
    else:
        hospitals = Hospital.objects.all()
    return render(request, 'listings/location_filter.html', {'hospitals': hospitals})
def filter_by_rating(request):
    rating = request.GET.get('rating')
    if rating:
        doctors = DoctorListing.objects.filter(rating__gte=rating)
    else:
        doctors = DoctorListing.objects.all()
    return render(request, 'listings/rating_filter.html', {'doctors': doctors})
def filter_by_availability(request):
    availability = request.GET.get('availability')
    if availability:
        doctors = DoctorListing.objects.filter(availability__icontains=availability)
    else:
        doctors = DoctorListing.objects.all()
    return render(request, 'listings/availability_filter.html', {'doctors': doctors})
def filter_by_hospital(request):
    hospital_id = request.GET.get('hospital')
    if hospital_id:
        doctors = DoctorListing.objects.filter(hospital__id=hospital_id)
    else:
        doctors = DoctorListing.objects.all()
    return render(request, 'listings/hospital_filter.html', {'doctors': doctors})
def filter_by_experience(request):
    experience = request.GET.get('experience')
    if experience:
        doctors = DoctorListing.objects.filter(experience__gte=experience)
    else:
        doctors = DoctorListing.objects.all()
    return render(request, 'listings/experience_filter.html', {'doctors': doctors})