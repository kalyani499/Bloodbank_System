from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='donors/', blank=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    disease = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class BloodRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=5)
    unit = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.patient.user.username


class BloodStock(models.Model):
    blood_group = models.CharField(max_length=5)
    unit = models.IntegerField(default=0)

    def __str__(self):
        return self.blood_group

