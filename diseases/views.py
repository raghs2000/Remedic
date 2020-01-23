from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Disease
from .forms import addDisease

# Create your views here.
def index(request):
	diseases = Disease.objects.all();
	return render(request, 'diseases/index.html', {'diseases': diseases,})

def addNewDisease(request):
    if request.method == "POST":
        form = addDisease(request.POST)
        if form.is_valid():
            disease = form.save(commit=False)
            disease.save()
            return redirect(index)
    else:
        form = addDisease()
    return render(request, 'diseases/add.html', {'form': form})

def viewDiseases(request):
    diseases = Disease.objects.all();
    return render(request, 'diseases/viewDiseases.html', {'diseases': diseases,})

def deleteDisease(request, diseaseName):
    Disease.objects.get(name=diseaseName).delete()
    return redirect(viewDiseases)