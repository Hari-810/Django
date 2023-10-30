from django import forms
from .models import BusTiming
import datetime

class BusTimingForm(forms.ModelForm):
    class Meta:
        model = BusTiming
        fields = '__all__'


"""
we define a BusTimingForm class that inherits from forms.ModelForm. 
This form is based on the BusTiming model and will automatically generate fields corresponding to the model's fields. 
The fields = '__all__' statement specifies that all fields from the model should be included in the form.
"""