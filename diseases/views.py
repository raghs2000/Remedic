from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Disease, Patient
from .forms import addDisease
import random
from .algorithm import scan, scan2

diseases = ['Cancer', 'Lupus', 'Hepatitis B']
congeniality = ['No', 'No', 'Yes']
classifications = ['Metabolical', 'Autoimmune', 'Infectious','hereditary']
blood_groups = ['O+', 'A+', 'AB-', 'A-','B+','B-','O-','AB+','B-']
allergies = ['Grapes', 'Peanuts', 'Lactose', 'Pollen','Dust', 'Bullshit']
preExistings = ['None', 'AIDS', 'Down','Turner']

# Create your views here.
def index(request):
	diseases = Disease.objects.all();
	return render(request, 'diseases/index.html',)

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


def addNewPatient(request):
    #for i in range(100):
        #name = 'Patient' + str(i + 300)
        #blood_group = blood_groups[random.randrange(0,9)]
        #age = str(random.randrange(1,100))
        #allergy = allergies[random.randrange(0,6)]
        #height = str(random.randrange(3,8))
        #preExisting = preExistings[random.randrange(0,4)]
        #history = diseases[random.randrange(0,3)]
        #patient = Patient(name=name,blood_group=blood_group,age=age,allergy=allergy,height=height,preExisting=preExisting,history=history)
        #patient.save()
    scan2()
    return redirect(index)

def viewDiseases(request):
    diseases = Disease.objects.all();
    return render(request, 'diseases/viewDiseases.html', {'diseases': diseases,})

def deleteDisease(request, diseaseName):
    Disease.objects.get(name=diseaseName).delete()
    return redirect(viewDiseases)