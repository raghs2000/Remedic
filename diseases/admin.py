from django.contrib import admin

from .models import Disease, Patient

admin.site.register(Disease)
admin.site.register(Patient)