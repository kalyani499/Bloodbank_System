from django.contrib import admin
from .models import *

admin.site.register(Donor)
admin.site.register(Patient)
admin.site.register(BloodRequest)
admin.site.register(BloodStock)
