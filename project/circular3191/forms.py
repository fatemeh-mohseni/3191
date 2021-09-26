from typing import Text
from django import forms 



class Input_form(forms.Form):

    project_name     = forms.CharField(max_length=100)
    building_name    = forms.CharField(max_length=100 )
    group            = forms.CharField()
    repetition      = forms.CharField(max_length=100)
    cost_per_meter   = forms.CharField(max_length=100, required=False)
    area             = forms.CharField(max_length=100, required=False)
    initial_estimate = forms.CharField(max_length=100, required=False)