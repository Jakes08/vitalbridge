from django.db import models

class DoctorListing(models.Model):
    name = models.CharField(max_length=120)
    specialization = models.CharField(max_length=120)
    rating = models.FloatField(default=0.0)
    contact_info = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    contact_info = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
