from django import forms
from Event_Registration.models import CustModel,EventModel

class Custforms(forms.ModelForm):
    class Meta:
        model=CustModel
        fields="__all__"

class Eventforms(forms.ModelForm):
    class Meta:
        model=EventModel
        fields="__all__"