from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Disease, Patient
from .forms import addDisease
import random

def scan(disease):
	patients = Patient.objects.all().filter(history=disease.name)
	return len(patients)

def scan2():
	diseases = Disease.objects.all();
	stats = ""
	for disease in diseases:
		patients = Patient.objects.all().filter(history=disease.name)
		stats += disease.name + " : " + str(len(patients)) + "\n"
	return stats