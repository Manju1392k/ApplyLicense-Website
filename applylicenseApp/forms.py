
from dataclasses import fields
from .models import ApplyLicense
from django.forms import ModelForm
from django import forms

class ApplyLicenseform(ModelForm):
    class Meta:
        model = ApplyLicense
        fields = ['Name','Age','Father_Name','Scc_Number','Adhar_Number']

    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Age = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Father_Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Scc_Number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Adhar_Number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))