from django import forms
from .models import Disease

congeniality = (('Yes', 'Yes'), ('No', 'No'))


class addDisease(forms.ModelForm):

    name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Name of Disease'}))
    congenial = forms.ChoiceField(choices=congeniality, label='')
    age_group = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Age Groups'}))
    classification = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Classification'}))
    causes = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Causes'}))
    preventions = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Preventions'}))
    treatment = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Treatments'}))

    class Meta:
        model = Disease
        fields = ['name', 'congenial', 'age_group', 'classification', 'causes', 'preventions', 'treatment']